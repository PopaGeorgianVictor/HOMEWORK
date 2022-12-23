
from BDD.pages.login_page import  LoginPage
from BDD.pages.home_page import  HomePage
from browser import Browser


def before_all(context):
    context.browser = Browser()
    context.home_page_object = HomePage()
    context.login_page_object = LoginPage()
    context.logout_page_object = LogoutPage()

def after_all(context):
    context.browser.close()