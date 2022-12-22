from selenium.webdriver.common.by import By
from BDD.pages.base_page import Base_page
from selenium.common import NoSuchElementException



class Logout_page(Base_page):

    LOGOUT_BTN = (By.CSS_SELECTOR, '.icon-2x.icon-signout')

    def click_on_logout(self):
        self.driver.find_element(*self.LOGOUT_BTN).click()
