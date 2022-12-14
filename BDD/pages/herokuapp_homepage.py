

from selenium.webdriver.common.by import By
from BDD.pages.base_page import Base_page

class Home_page(Base_page):
    FORM_BTN = ()


    def navigate(self):
        self.driver.get()

    def adsd(self)
        self.driver.find_element(*self.FORM_BTN).click()




