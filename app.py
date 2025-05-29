from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    
    # Launch the browser
    browser = playwright.chromium.launch(headless=False, slow_mo=5000)
    playwright.chromium.launch()
    
    # Create a new page
    page = browser.new_page()
    # Visit a website
    page.goto("https://playwright.dev/python/docs/intro")
    # hover_element = page.get_by_label("navbar__item dropdown dropdown--hoverable") # get_by_role("link", name="Java", exact=True)
    xpath_element = page.locator('xpath=//*[@id="__docusaurus"]/nav/div[1]/div[1]/div').hover()
    
    docs_button = page.get_by_role("link", name="Java", exact=True)
    docs_button.click()
    
    # get the url and print it
    print("Docs url:", page.url)
    # context = browser.new_context()
    # page = context.new_page()

    # Wait for the element to be visible
    # page.wait_for_selector("#element_id", state="visible")

    # Click the element
    # page.click("#element_id")

    page.goto("https://bootswatch.com/default/")
    email_input = page.get_by_label("Email address")
    email_input.highlight()
    page.get_by_label("Password").highlight()
    page.get_by_label("Example textarea").highlight()
    
    page.get_by_placeholder("Enter email").highlight()
    
    page.get_by_placeholder("Password").highlight()
    page.get_by_title("Password").highlight()
    page.get_by_text
    # Close the browser
    browser.close()
    
