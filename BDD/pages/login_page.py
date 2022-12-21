from selenium.webdriver.common.by import By
from BDD.pages.base_page import Base_page

class Login_page(Base_page):

    USERNAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    LOGIN_BTN = (By.CSS_SELECTOR, '.fa.fa-2x.fa-sign-in')

    def complete_field(self):
        self.driver.find_element(*self.USERNAME).send_keys("tomsmith")
        self.driver.find_element(*self.PASSWORD).send_keys("SuperSecretPassword!")

    def login(self):
        self.driver.find_element(*self.LOGIN_BTN).click()

    def redirect_to_secure(self):
