from behave import *

@when('I clicked on Logout button')
def step_impl(context):
    context.logout_page_object.logout()

@then("I successfully logout and redirect to the '/login' page and info message ' You logged out of the secure area!' is displayed in a green tab")
def step_impl(context):
    context.logout_page_object.redirect_to_login_page()
    context.logout_page_object.info_msg()