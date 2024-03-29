''' Implements a login class to inherit unittest.Testcase

Find the items at the top using what selectors you want:

- Setup ()
- Driver
https://the-internet.herokuapp.com/
Click on Form Authentication

teardown ()
Quit browser

● Test 1
- Check if the new URL is correct

● Test 2
- Check if Page Title is correct

● Test 3
- Check the text on the item xpath = // h2 is correct

● Test 4
- Check if the login button is displayed

● Test 5
- Check if the Href attribute of the 'Elemental Selenium' link is correct

● Test 6
- Leave empty user and pass
- Click Login
- Check if the error is displayed

● Test 7
- Complete with User and Pass Invalid
- Click Login
- Check if the message on the error is correct
- there is an x put there so we will use the solution below
expected = 'your username is invalid!'
Self.asserttrue (expected in the current incorrect ')

● Test 8
- Leave empty user and pass
- Click Login
- Press x to error
- Check if the error has disappeared

● Test 9
- take as a list all // label
- checks the text that the text on them is expected (username and
Password)
- Here's ok to have 2 asserts

● Test 10
- Complete with Valid User and Pass
- Click Login
- check that the new URL contains /Secure
- Use an explicit Wait for the element with the 'Flash success' class
- Check if the element with class = 'Flash success' is displayed
- Check if the message on this element contains the text 'Secure Area!'

● Test 11
- Complete with Valid User and Pass
- Click Login
- Click Logout
- Check if you arrived on https://the-internet.herokuapp.com/login

● Test 12 - Brute Force Password Hacking
- Complete User tomsmith
- Find the item //h4
- Take the text from him and spit after space. Considers every word as a potential password
- uses an iterative structure by which to enter a row passwords and press on the login
- Finally the test must print:
'I failed to find the password'
  or
'The secret password is [password]'
'''


import unittest
import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By



class Login(unittest.TestCase):
    LOGIN_BTN = (By.XPATH, '//*[@id="login"]/button/i')
    USERNAME = (By.XPATH, '//input[@id="username"]')
    PASSWORD = (By.XPATH, '//input[@id="password"]')
    LOGIN_INFO = (By.XPATH, "//h4")


    def setUp(self) -> None:
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://the-internet.herokuapp.com/")
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[21]/a').click()

    def tearDown(self) -> None:
        self.driver.quit()

    # TEST 1
    def test_url(self):
        actual = self.driver.current_url
        expected = 'https://the-internet.herokuapp.com/login'
        # assertEqual() to check equality of first & second value
        self.assertEqual(actual, expected, 'URL is incorect')

    # TEST 2
    def test_page_title(self):
        actual = self.driver.title
        print('The title of the page is: ' , actual)
        expected = 'The Internet'
        self.assertEqual(expected, actual, 'Page title is incorrect')

    # TEST 3
    def test_h2_text(self):
        actual = self.driver.find_element(By.XPATH, '//h2').text
        print('Text of the //h2 element is: ', actual)
        expected = 'Login Page'
        self.assertEqual(expected, actual, 'Text is incorrect')


    # TEST 4
    def test_login_btn_visible(self):
        lg_btn = self.driver.find_element(*self.LOGIN_BTN)
        # assertTrue() to check true of test value
        self.assertTrue(lg_btn.is_displayed(), "I don't see the login button!!!")

    # TEST 5
    def test_elem_atribute(self):
        actual = self.driver.find_element(By.XPATH, '//*[@id="page-footer"]/div/div/a').get_attribute('href')
        # get href attribute
        print('LINK:', actual)
        expected = 'http://elementalselenium.com/'
        self.assertEqual(expected, actual, 'Elemental Selenium button href attribute is wrong')

    # TEST 6
    def test_empty_user_password(self):
        self.driver.find_element(*self.LOGIN_BTN).click()
        error = self.driver.find_element(By.XPATH, '//*[@id="flash"]')
        self.assertTrue(error.is_displayed(), 'Error is not here!!!')

    # TEST 7
    def test_error_invalid_user_pass(self):
        self.driver.find_element(By.ID, 'username').send_keys('sound check, sound check')
        self.driver.find_element(By.ID, 'password').send_keys('microfonul e suspect')
        self.driver.find_element(*self.LOGIN_BTN).click()
        actual = self.driver.find_element(By.XPATH, '//*[@id="flash"]').text
        print('Message error is:', actual)
        expected = 'Your username is invalid!'
        self.assertTrue(expected in actual, 'Error message text is incorrect')

    # TEST 8
    def test_close_error(self):
        self.driver.find_element(*self.LOGIN_BTN).click()
        self.driver.find_element(By.XPATH, '//*[@id="flash"]/a').click()  # close the error
        error = self.driver.find_element(By.XPATH,'//*[@id="flash"]')
        self.assertTrue(error.is_displayed(),'Error is not displayed')

    # TEST 9
    def test_labels(self):
        label_result1 = self.driver.find_element(By.XPATH, '//label[@for="username"]').text
        assert label_result1 == "Username"
        label_result2 = self.driver.find_element(By.XPATH, '//label[@for="password"]').text
        assert label_result2 == "Password"

    # TEST 10
    def test_valid_user_pas(self):
        self.driver.find_element(By.ID, 'username').send_keys('tomsmith')
        self.driver.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')
        self.driver.find_element(*self.LOGIN_BTN).click()
        actual_url = self.driver.current_url
        expected_url = 'https://the-internet.herokuapp.com/secure'
        self.assertEqual(expected_url, actual_url, 'URL is incorrect')
        elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'flash')))
        elem = self.driver.find_element(By.CLASS_NAME, 'success')
        self.assertTrue(elem.is_displayed(), 'SUBMIT BTN is not there!!!')
        actual_msg = self.driver.find_element(By.CLASS_NAME, 'success').text
        expected_msg = 'secure area'
        self.assertTrue(expected_msg in actual_msg, 'Page title is incorrect')


    # TEST 11
    def test_login_logout(self):
        self.driver.find_element(By.ID, 'username').send_keys('tomsmith')
        self.driver.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')
        self.driver.find_element(*self.LOGIN_BTN).click()
        self.driver.find_element(By.XPATH, '//*[@id="content"]/div/a/i').click()
        actual_url = self.driver.current_url
        expected_url = 'https://the-internet.herokuapp.com/login'
        self.assertEqual(expected_url, actual_url, 'URL is incorrect')

    # TEST 12

    # method 1
    def hacking(self):
        brelock = self.driver.find_element(By.XPATH, '//h4').text.split()
        master_key = None
        i = 0
        while ((i < len(brelock)) and (master_key == None)):
            self.driver.find_element(By.ID, 'username').send_keys('tomsmith')
            self.driver.find_element(By.ID, 'password').send_keys(brelock[i])
            self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
            self.driver.implicitly_wait(2)
            try:
                self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').is_displayed()
            except NoSuchElementException:
                master_key = brelock[i]
                break
            i += 1
            self.driver.find_element(By.ID, 'username').clear()
            self.driver.find_element(By.ID, 'password').clear()
        if master_key != None:
            print(f"Hacking complete: {master_key}")
        else:
            print('Hacking failed')



     # method 2
    def test_brute_force_password_hacking(self):
        login_message_split = self.driver.find_element(*self.LOGIN_INFO).text.split()
        for word in login_message_split:
            self.driver.find_element(*self.USERNAME).send_keys("tomsmith")
            self.driver.find_element(*self.PASSWORD).send_keys(word)
            self.driver.find_element(*self.LOGIN_BTN).click()
            if "secure" in self.driver.current_url:
                print(f"Hacking complete:  {word}")
                break
        assert "secure" in self.driver.current_url, "Hacking failed"


if __name__ == '__main__' :
    unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output='D:/selenium project/HOMEWORK/report'))








