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


    # Some deeper test cases Im thinking of (ChestnutFi real world use cases):
    # 1. Onboarding: Integration with the National Insurance Producer Registry (NIPR), 
    #      producer self-service tools, automated workflows, and API ingestion.
    # 2. Hierarchy Management: Unlimited, rules-based configurations with effective dating.
    # 3. Debt Management & Collections: Automated monitoring and detailed reporting of debts.
    # 4. Incentive Compensation: Strategic plan design, pay-for-performance, and non-monetary incentives. 
    # 5. Insights Framework: Custom KPIs for producer rating, ranking, and performance improvements.
    
    # API Integration testing: 
    # 1. Add or retrieve producer (John agent) details (Correct GET POST status codes, payloads)
    # 2. Assign producers to teams or regions
    # 3. Trigger compensation calculations
    # 4. Fetch performance metrics (Data validation (types, formats))
    # 5. Validate licensing through external sources like NIPR (Data validation)
    #   5.1. Validate producer's license status 
    #   5.2. License and Appointment Tracking.
    #   5.3. License Management and Renewal.
    #   5.4. Ensure License in the Producer Database 
    #   5.5. Access and Integration Features related to NIPR and ChestnutFi integration.
    # 6. Security or access control of the Chestnut's API (Authentication, Authorization) 
    
    # 7. SQL Injection testing:
    #    7.1. Test for SQL injection vulnerabilities (SELECT * FROM Users WHERE Name ="" or ""="" AND Pass ="" or ""="")
    #    7.2. Test for SQL injection vulnerabilities in the API (GET POST requests)
    # 8. Cross-Site Scripting (XSS) testing:
    #    8.1. Test for XSS vulnerabilities in the API (GET POST requests)
    # 9. Performance testing:
    #    9.1. Test the performance of the API (GET POST requests)
    # 10. Load testing:
    #     10.1. Test the load capacity of the API (GET POST requests)
    # 11. Security testing: 
    #     11.1. Test the security of the API (GET POST requests)
    # 12. Usability testing:
    #     12.1. Test the usability of the API (GET POST requests)
    
    # Data validation most likely on the backend side: 
    # 1. Validate producers data (e.g., name, license number, contact details)
    # 2. Validate Bonus & Commission Structures (Rules, Eligibility, Bonus formulas, Payment schedules, Audit logs of payouts)
    # 3. Validate Regions and Teams (Region names, Team manager mappings and structures, Hierarchical relationships, Grouping for performance analytics)
    # 4. Validate Bonus/Commission Records (Producer ID, Bonus type, amount, calculation source, Approval or payout status) 
    #       Not stored by Chestnut (external/integrated data)
    # 1. Validate Licenses API responses (Fetched from NIPR, License numbers, expiration, states, license types)
    # 2. Validate Payroll/Accounting Data (Final payouts should be handled by external payroll systems, like QuickBooks, ADP, Workday etc.)
    # 3. Sales or Performance Metrics (in case integraion with Salesforce, some performance inputs could be puuled from Chestnut, like deal size or revenue won)
    
'''
        [External Licensing API]
             (e.g., NIPR)
                   │                  Licenses QA: API sync, expiry logic, fallback if missing  
            [License Info]                  Edge Case: Expired or missing licenses
                   │    
                   ▼                    
              [Producers]◀────────────┐ QA Producers data: Input validation, uniqueness, sync w/ licenses
               (Core Entity)          │     Edge Case: Producers switched teams mid-quarter
                   │                  │
     ┌─────────────┼────────────┐     │
     ▼             ▼            ▼     │
 [Regions]   [Bonus Plans]  [Commission Structures]   QA: Formula logic, floating point precision, eligibility
     │             │            │     │                     Edge Case: Negative commissions (chargebacks)
     ▼             ▼            ▼     │
[Hierarchy]   [Eligibility]   [Calculations]    QA: Cross-Module Integrity 
                   │                  │             Edge Case: Missing bonus plan for a producer, Manual overrides by admins
                   └─────┬────────────┘
                         ▼
               [Bonus/Commission Records]    QA: Timestamping, duplicates, data rollbacks
                         │                      Edge Case: Missing records after a system crash
                         ▼
              [External Payroll System]     QA: Data export, formatting, totals match Chestnut
                 (e.g., ADP, QuickBooks)        Edge Case: Missing payroll entries for a producer
'''

# Onboarding Workflow — P0 test cases:
# Scenario: Successful Producer Onboarding with Valid License.
    # 1. Submit onboarding form with valid personal + license info
    # 2. System pulls license from NIPR
    # 3. Assign to region/team
    # 4. Confirm status as “Active”
    # 5. Verify producer visible in dashboard/API/search
# Scenario: Incentive (Bonus) Calculation — P0: Producer Hits Target and Receives Correct Bonus
    # 1. Producer generates $60K sales in Q2
    # 2. Run bonus calculation job
    # 3. Bonus payout is recorded correctly
# Scenario: Mid-Quarter Team Change — Bonus Split or Blocked
    # 1. Producer moves from Region A to Region B mid-Q  -> Verify Clear rule on split/eligibility -> System applies correct logic
    # 2. Region A hits target, Region B does not  -> Final bonus reflects correct region/team logic
    # 3. Check if bonus is correctly prorated or disqualified  -> UI shows reason if disqualified
# 
# Key QA Priorities: 
# - Onboarding:	License validation, duplicate detection
# - Bonus Logic	Accuracy, thresholds, disqualification
# - Edge Cases:	Manual overrides, region changes
# - Data Flow:	API → DB → UI → Export consistency 
#
#
#