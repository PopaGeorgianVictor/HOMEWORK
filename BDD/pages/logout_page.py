from selenium.webdriver.common.by import By
from BDD.pages.base_page import Base_page
from selenium.common import NoSuchElementException



class Logout_page(Base_page):

    LOGOUT_BTN = (By.CSS_SELECTOR, '.icon-2x.icon-signout')
    LOGIN_BTN = (By.CSS_SELECTOR, '.fa.fa-2x.fa-sign-in')
    INFO_MSG = (By.ID, 'flash')
    def logout(self):
        self.driver.find_element(*self.LOGOUT_BTN).click()

    def redirect_to_login_page(self):
        try:
            self.driver.find_element(*self.LOGIN_BTN)
            print('Element exist')

        except NoSuchElementException:
            print("Element does not exist")

    def info_msg(self):
        info_msg_text = self.driver.find_element(*self.INFO_MSG).text
        expected_text = "You logged out of the secure area!"
        assert info_msg_text == expected_text, f"Error: expected: {expected_text}, actual: {info_msg_text}"
