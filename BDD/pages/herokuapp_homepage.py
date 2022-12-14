

from selenium.webdriver.common.by import By
from BDD.pages.base_page import Base_page

class Home_page(Base_page):
    FORM_BTN = ()


    def navigate_to_page(self):
        self.driver.get()

    def click_on_form(self)
        self.driver.find_element(*self.FORM_BTN).click()




