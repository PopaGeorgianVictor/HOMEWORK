from behave import *

@when("I enter correct username and password")
def step_impl(context):
    context.login_page_object.complete_field()