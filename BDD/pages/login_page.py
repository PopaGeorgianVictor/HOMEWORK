
from BDD.pages.base_page import Base_page
class Home_page(Base_page):

    USERNAME = ()
    PASSWORD = ()
    LOGIN_BTN = ()

    def complete_field(self):
        self.driver.find_element(*self.USERNAME).send_keys("tomsmith")
        self.driver.find_element(*self.PASSWORD).send_keys("SuperSecretPassword!")

    def login(self):
        self.driver.find_element(*self.LOGIN_BTN).click()


