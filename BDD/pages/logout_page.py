from selenium.webdriver.common.by import By
from BDD.pages.base_page import Base_page
from selenium.common import NoSuchElementException



class Logout_page(Base_page):

    LOGOUT_BTN = (By.CSS_SELECTOR, '.icon-2x.icon-signout')
    LOGIN_BTN = (By.CSS_SELECTOR, '.fa.fa-2x.fa-sign-in')
    def logout(self):
        self.driver.find_element(*self.LOGOUT_BTN).click()

    def redirect_to_login_page(self):
        try:
            self.driver.find_element(*self.LOGIN_BTN)
            print('Element exist')

        except NoSuchElementException:
            print("Element does not exist")
