from behave import *

@when("I enter correct username and password")
def step_impl(context):
    context.login_page_object.complete_field()

@when("I clicked on Login button")
def step_impl(context):
    context.login_page_object.login()

@then("I successfully enter on '/secure' page")
def step_impl(context):
    context.