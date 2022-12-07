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
- Finally the test must printe:
'I failed to find the password'
or
'The secret password is [password]'
'''
import unittest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


class Login(unittest.TestCase):
    LOGIN_BTN = (By.XPATH, '//*[@id="login"]/button/i')
    USERNAME = (By.XPATH, '//input[@id="username"]')
    PASSWORD = (By.XPATH, '//input[@id="password"]')

    def setUp(self) -> None:
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
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














