from behave import *

@when("I enter correct username and password")
def step_impl(context):
    context.login_page_object.complete_field()

@when("I clicked on Login button")
def step_impl(context):
    context.login_page_object.login()

@then("I successfully enter on '/secure' page and info message 'You logged into a secure area!' is displayed in a green tab")
def step_impl(context):
    context.login_page_object.enter_to_secure()
    context.login_page_object.info_msg()