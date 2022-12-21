
from behave import *

@given("I am on herokuapp homepage")
def step_impl(context):
    context.home_page_object.navigate_to_page()

@when("I click on Form Authentication")
def step_impl(context):
    context.home_page_object.click_on_form()

@then("I am able to enter on page")
def step_impl(context):
    context.home_page_object.redirect_to_login_page()

