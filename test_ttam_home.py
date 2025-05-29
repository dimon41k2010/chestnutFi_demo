import pytest
from playwright.sync_api import sync_playwright

USERNAME = "dmytro.gordiienko@gmail.com"
PASSWORD = "Dimon41k!"
LOGIN_URL = "https://ads.tiktok.com/i18n/login"
HOME_URL = "https://ads.tiktok.com/i18n/home/"
STORAGE_STATE = "tiktok_state.json"

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=700)
        yield browser
        browser.close()

@pytest.fixture(scope="session")
def save_storage_state(browser):
    # Only run this once to save the storage state after manual login
    context = browser.new_context()
    page = context.new_page()
    page.goto(LOGIN_URL)
    page.fill('input[name="email"]', USERNAME)
    page.fill('input[name="password"]', PASSWORD)
    page.click('button:has-text("Log in")')
    # Wait for manual puzzle solving and successful login
    print("Please solve the puzzle manually in the opened browser window.")
    page.wait_for_url(HOME_URL, timeout=12000)  # Wait up to 2 minutes
    context.storage_state(path=STORAGE_STATE)
    context.close()

@pytest.fixture
def page(browser, save_storage_state):
    # Use the saved storage state to skip login and puzzle
    context = browser.new_context(storage_state=STORAGE_STATE)
    page = context.new_page()
    yield page
    context.close()

def test_login_success(page):
    page.goto(HOME_URL)
    assert HOME_URL in page.url
    # Adjust the selector below if "Dashboard" is not visible after login
    assert page.locator("text=Dashboard").is_visible()