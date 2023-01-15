
from BDD_herokuapp.pages.login_page import  LoginPage
from BDD_herokuapp.pages.home_page import  HomePage
from BDD_herokuapp.pages.logout_page import LogoutPage
from browser import Browser


def before_all(context):
    context.browser = Browser()
    context.home_page_object = HomePage()
    context.login_page_object = LoginPage()
    context.logout_page_object = LogoutPage()

def after_all(context):
    context.browser.close()