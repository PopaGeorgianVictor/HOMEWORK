from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service


class Browser():
    driver = webdriver.Chrome(service=Service(GeckoDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(2)



    def close(self):
        self.driver.delete_all_cookies()
        self.driver.quit()
