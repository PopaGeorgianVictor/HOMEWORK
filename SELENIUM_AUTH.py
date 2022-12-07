
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service


class Authentication_in_Firefox(unittest.TestCase):

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