
import time
import unittest
import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service


class ContextMenu(unittest.TestCase):

		BOX = (By.ID,"hot-spot")
		def setUp(self) -> None:
				self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
				self.driver.maximize_window()
				self.driver.get("https://the-internet.herokuapp.com/context_menu")
				self.driver.implicitly_wait(2)

		def tearDown(self) -> None:
				self.driver.quit()

		def test_context(self):
				action = ActionChains(self.driver)
				elem = self.driver.find_element(*self.BOX)
				action.context_click(elem).perform()
				time.sleep(3)
				self.driver.switch_to.alert.accept()
				time.sleep(2)

if __name__ == '__main__' :
	unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output='D:/selenium project/HOMEWORK/report'))