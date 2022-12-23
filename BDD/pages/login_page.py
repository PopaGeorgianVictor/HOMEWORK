from selenium.webdriver.common.by import By
from BDD.pages.base_page import BasePage
from selenium.common import NoSuchElementException
import time

class LoginPage(BasePage):

    USERNAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    LOGIN_BTN = (By.CSS_SELECTOR, '.fa.fa-2x.fa-sign-in')
    LOGOUT_BTN =(By.CSS_SELECTOR, '.icon-2x.icon-signout')
    INFO_MSG = (By.ID, 'flash')


    def complete_field(self):
        self.driver.find_element(*self.USERNAME).send_keys("tomsmith")
        self.driver.find_element(*self.PASSWORD).send_keys("SuperSecretPassword!")

    def login(self):
        self.driver.find_element(*self.LOGIN_BTN).click()

    def enter_to_secure(self):
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])
        print("Second window title = " + self.driver.title)
        try:
            self.driver.find_element(*self.LOGOUT_BTN)
            print('Element exist')

        except NoSuchElementException:
            print("Element does not exist")

    def info_msg(self):
        info_msg_text = self.driver.find_element(*self.INFO_MSG).text
        expected_text = " You logged into a secure area!"
        assert info_msg_text == expected_text, f"Error: expected: {expected_text}, actual: {info_msg_text}"

