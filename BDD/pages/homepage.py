from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from BDD.pages.base_page import Base_page
import time


class Home_page(Base_page):
    FORM_BTN = (By.CSS_SELECTOR, "a[href='/login']")
    LOGIN_BTN = (By.CSS_SELECTOR, '.fa.fa-2x.fa-sign-in')

    def navigate_to_page(self):
        self.driver.get()

    def click_on_form(self):
        self.driver.find_element(*self.FORM_BTN).click()

    def redirect_to_login_page(self):
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[1])
        print("Second window title = " + driver.title)
        try:
            self.driver.find_element(*self.LOGIN_BTN)
            print('Element exist')

        except NoSuchElementException:
            print("Element does not exist")



