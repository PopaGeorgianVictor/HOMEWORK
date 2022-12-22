from behave import *

@when('I clicked on Logout button')
def step_impl(context):
    context.logout_page_object.logout()