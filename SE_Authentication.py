
import unittest
import HTMLTestRunner
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

class Authentication(unittest.TestCase):

		USERNAME = 'admin'
		PASSWORD = 'admin'
		def setUp(self) -> None:
				self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
				self.driver.maximize_window()
				self.driver.get("https://the-internet.herokuapp.com/context_menu")
				self.driver.implicitly_wait(2)

		def tearDown(self) -> None:
				self.driver.quit()

		def test_auth(self):
				self.driver.get('https://' + self.USERNAME + ':' + self.PASSWORD + '@the-inernet.herokuapp.com/basic_auth')


if __name__ == '__main__' :
	unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output='D:/selenium project/HOMEWORK/report'))

