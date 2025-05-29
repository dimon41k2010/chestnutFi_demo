from behave import *

@given("User on the homepage"):
def step_1(context):
    pass
@then("User should see the navbar"):
def step_2(context):
    assert context.browser_page.locator("text='Key Features'").is_visible(), "Key Features section is not visible"
    assert context.browser_page.locator("text='Revenue Centric'").nth(1).is_visible(), "Revenue Centric feature is not visible"