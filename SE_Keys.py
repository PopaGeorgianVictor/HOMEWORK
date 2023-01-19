
import time
import unittest
import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager


class Keyboard(unittest.TestCase):

		USERNAME = (By.ID,"username")

		def setUp(self) -> None:
				self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
				self.driver.maximize_window()
				self.driver.get("https://the-internet.herokuapp.com/login")
				self.driver.implicitly_wait(2)

		def tearDown(self) -> None:
				self.driver.quit()

		def test_select_all(self):
				user = self.driver.find_element(*self.USERNAME)
				user.send_keys("anton")
				time.sleep(2)
				user.clear()
				user.send_keys("tmsmith")
				time.sleep(2)
				user.send_keys(Keys.COMMAND,'a')
				user.send_keys(Keys.BACKSPACE)
				user.send_keys("tmsmith")
				time.sleep(2)
				user.send_keys(Keys.ARROW_LEFT)
				time.sleep(2)


if __name__ == '__main__' :
	unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output='D:/selenium project/HOMEWORK/report'))