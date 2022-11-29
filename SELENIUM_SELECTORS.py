'''Choose 3 items from each selector type from the following categories:
● Id
● Text link
● Partial text link
● Name
● Tag*
● Class name*
● Css (1 by id, 1 by class, 1 by attribute=partial_value)

Observation:

- You probably won't find a single website that includes all the options
above, so we recommend that you use multiple sites
- Optional: For tag and class name you will use find elements! - save to list.
Interact with an item of your choice from the list

For xpath identify elements according to the criteria below:
● 3 by value attribute
● 3 after the text on the element
● 1 after partial text
● 1 with OR, using pipe |
● 1 with *
● 1 where you take them as a list of xpath and in python it ends up 1 element, so
with (xpath)[1]
● 1 in which to use parent::
● 1 in which to use the brother before or after (your choice)
● 1 function like the one in the class by which I can choose by parameter with
which element I want to interact with.
'''

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


url = 'https://www.techlistic.com/p/selenium-practice-form.html'

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get(url)
driver.maximize_window()

# this is for accepting Cookies
driver.find_element(By.ID, 'ez-accept-all').click()


# find element By.ID

driver.find_element(By.ID, 'sex-0').click()
driver.find_element(By.ID, 'exp-0').click()
driver.find_element(By.ID, 'datepicker').send_keys('29.11.2022')



# find element By.NAME

driver.find_element(By.NAME, 'firstname').send_keys('Popa')
driver.find_element(By.NAME, 'lastname').send_keys('Georgian')
driver.find_element(By.NAME, 'profession').click()

# find element By.LINK_TEXT

driver.find_element(By.LINK_TEXT, 'Top 7 Web Development Trends').click()
driver.find_element(By.LINK_TEXT, 'How I learned Selenium in 4 weeks').click()
driver.find_element(By.LINK_TEXT, 'A Complete Guide to API Development').click()

# find element By.PARTIAL_LINK_TEXT

driver.find_element(By.PARTIAL_LINK_TEXT ,'Development').click()
driver.find_element(By.PARTIAL_LINK_TEXT ,'Selenium').click()
driver.find_element(By.PARTIAL_LINK_TEXT ,'API').click()
