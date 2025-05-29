import re
from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright

def test_basic():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.skyscanner.com")
        assert page.title() == "Compare Cheap Flights & Book Airline Tickets to Everywhere | Skyscanner"
        browser.close()

# def test_has_title(browser_page):
#     browser_page.goto("https://playwright.dev/")
#     expect(browser_page).to_have_title(re.compile("Playwright"))

# def test_get_started_link(browser_page):
#     browser_page.goto("https://playwright.dev/")
#     browser_page.get_by_role("link", name="Get started").click()
#     expect(browser_page.get_by_role("heading", name="Installation")).to_be_visible()

