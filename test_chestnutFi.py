import pytest
import datetime
from time import sleep
from playwright.sync_api import sync_playwright

# test_app.py
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

@pytest.fixture(scope="function")
def browser_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        yield page
        browser.close()

def test_homepage_title_contains_chestnut(browser_page):
    browser_page.goto("https://www.chestnutfi.com/")
    assert "Chestnut" in browser_page.title()

# @pytest.mark.parametrize(("num", "expected"), ((1,1), (2, 2), (3, 3)))
def test_signup_button_present(browser_page):
    browser_page.goto("https://www.chestnutfi.com/")
    # Try common button texts, update selector if needed
    assert browser_page.locator("text='Features'").is_visible() or browser_page.locator("text='About'").is_visible()

def test_navigation_menu_items(browser_page):
    browser_page.goto("https://www.chestnutfi.com/")
    # Check for common navigation items
    nav_items = ["Features", "About", "Resources", "Let's talk"]
    for item in nav_items:
        assert browser_page.locator(f"text='{item}'").first.is_visible()
    
    browser_page.locator(f"text='{nav_items[0]}'").click()
    
    # Check if the page has the Key Features section
    assert browser_page.locator("text='Key Features'").is_visible()
    assert browser_page.locator("text='Revenue Centric'").nth(1).is_visible()
    
    # Check if the CTA button using XPath is visible and has correct text
    p_xpath = browser_page.locator("xpath=/html/body/section[7]/div/div[2]/a/p") # secondary button /html/body/section[6]/div/div[1]/a/p
    assert p_xpath.is_visible()
    assert p_xpath.text_content().strip() == "See the platform in action"
    
    # Click the CTA button
    p_xpath.click()
    
    # Take a screenshot and save it to the Downloads folder
    # browser_page.screenshot(path="./Screenshots/chestnut_test_screenshot.png", full_page=True)
    screenshot_path = f"{'./Screenshots/chestnut_test_screenshot_'}{timestamp}.png"
    browser_page.screenshot(path=screenshot_path, full_page=True)
    
    # Fill up the form
    browser_page.fill("input[name='Contact-6-First-Name']", "Big John")
    browser_page.fill("input[name='Contact-6-Last-Name']", "Smith") 
    browser_page.fill("input[name='Contact-6-Email']", "big.john@example.com")
    browser_page.fill("input[name='Contact-6-Org']", "Chestnut QA")
    browser_page.fill("input[name='Contact-6-Email-2']", "1234567890")
    browser_page.fill("input[name='Contact-6-Org-2']", "https://linkedin.com/in/bigjohn")
    browser_page.fill("textarea[name='Contact-6-Message']", "This is a test message.")

    assert "Contact" in browser_page.title()
    assert "https://www.chestnutfi.com/contact" in browser_page.url
    sleep(1)
    browser_page.screenshot(path=screenshot_path, full_page=True)
    
    print("test :", browser_page.url)
    
    
    
    
    
    # some deeper test cases Im thinking of (ChestnutFi landing page): Junior QA :)
    # 1. Check if the "Let's talk" button is visible and clickable
    # 2. Check if the "Let's talk" button redirects to the correct URL
    # 3. Check if the "Let's talk" button has the correct text
    # 4. Check if the "Let's talk" button has the correct role
    # 5. Check if the "Let's talk" button has the correct class
    # 6. Check if the "Let's talk" button has the correct aria-label
    # 7. Check if the "Let's talk" button has the correct aria-labelledby
    # 8. Check if the "Let's talk" button has the correct aria-describedby

