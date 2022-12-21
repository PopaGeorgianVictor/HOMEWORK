
from behave import *

@given("I am on herokuapp homepage")
def step_impl(context):
    context.home_page_object.navigate_to_page()