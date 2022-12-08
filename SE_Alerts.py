
import unittest
import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

class Alerts(unittest.TestCase):

		JS_ALERT = (By.CSS_SELECTOR,"[onclick='jsAlert()']") # alternativa XPATH: //*[@onclick="jsAlert()"]
		JS_ALERT_TEXT = (By.ID,"result")
		JS_CONFIRM = (By.CSS_SELECTOR,"[onclick='jsConfirm()']")
		JS_PROMPT = (By.CSS_SELECTOR,"[onclick='jsPrompt()']")
		INSERTED_TEXT = "test"


		def setUp(self) -> None:
				self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
				self.driver.maximize_window()
				self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")
				self.driver.implicitly_wait(2)

		def tearDown(self) -> None:
				self.driver.quit()


		# @functionalTesting @positiveTesting
		# use decorators to skip test
		@unittest.skip
		def test_js_alert_acccept(self):
				self.driver.find_element(*self.JS_ALERT).click()
				js_alert = self.driver.switch_to.alert
				js_alert.accept()
				js_alert_text = self.driver.find_element(*self.JS_ALERT_TEXT).text
				expected_text = "You successfully clicked an alert"
				assert js_alert_text == expected_text,f"Error: expected: {expected_text}, actual: {js_alert_text}"



		def test_js_confirm_accept_alert(self):
				self.driver.find_element(*self.JS_CONFIRM).click()
				js_confirm = self.driver.switch_to.alert
				js_confirm.accept()
				js_confirm_text = self.driver.find_element(*self.JS_ALERT_TEXT).text
				expected_text = "You clicked: Ok"
				assert js_confirm_text == expected_text,f"Error: expected: {expected_text}, actual: {js_confirm_text}"


		def test_js_confirm_cancel_alert(self):
				self.driver.find_element(*self.JS_CONFIRM).click()
				js_confirm = self.driver.switch_to.alert
				js_confirm.dismiss()
				js_confirm_text = self.driver.find_element(*self.JS_ALERT_TEXT).text
				expected_text = "You clicked: Cancel"
				assert js_confirm_text == expected_text,f"Error: expected: {expected_text}, actual: {js_confirm_text}"


		def test_js_prompt_accept_alert_with_text(self):
				self.driver.find_element(*self.JS_PROMPT).click()
				js_prompt = self.driver.switch_to.alert
				js_prompt.send_keys(self.INSERTED_TEXT)
				js_prompt.accept()
				js_prompt_text = self.driver.find_element(*self.JS_ALERT_TEXT).text
				expected_text = f"You entered: {self.INSERTED_TEXT}"
				assert js_prompt_text == expected_text, f"Error: expected: {expected_text}, actual: {js_prompt_text}"


		def test_js_prompt_cancel_alert_with_text(self):
				self.driver.find_element(*self.JS_PROMPT).click()
				js_prompt = self.driver.switch_to.alert
				js_prompt.send_keys(self.INSERTED_TEXT)
				js_prompt.dismiss()
				js_prompt_text = self.driver.find_element(*self.JS_ALERT_TEXT).text
				expected_text = "You entered: null"
				assert js_prompt_text == expected_text, f"Error: expected: {expected_text}, actual: {js_prompt_text}"


		def test_js_prompt_accept_alert_without_text(self):
				self.driver.find_element(*self.JS_PROMPT).click()
				js_prompt = self.driver.switch_to.alert
				js_prompt.accept()
				js_prompt_text = self.driver.find_element(*self.JS_ALERT_TEXT).text
				expected_text = f"You entered:"
				assert js_prompt_text == expected_text, f"Error: expected: {expected_text}, actual: {js_prompt_text}"

		# @functionalTesting @positiveTesting
		def test_js_prompt_cancel_alert_without_text(self):
				self.driver.find_element(*self.JS_PROMPT).click()
				js_prompt = self.driver.switch_to.alert
				js_prompt.dismiss()
				js_prompt_text = self.driver.find_element(*self.JS_ALERT_TEXT).text
				expected_text = f"You entered: null"
				assert js_prompt_text == expected_text, f"Error: expected: {expected_text}, actual: {js_prompt_text}"



if __name__ == '__main__' :
	unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output='D:/selenium project/HOMEWORK/report'))


