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
url1 = 'https://formy-project.herokuapp.com/form'

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(3)


# find_element(By.ID)

driver.get(url)
# this is for accepting Cookies
driver.find_element(By.ID, 'ez-accept-all').click()

driver.find_element(By.ID, 'sex-0').click()
driver.find_element(By.ID, 'exp-0').click()
driver.find_element(By.ID, 'datepicker').send_keys('29.11.2022')




# find_element(By.NAME)

driver.get(url)
# this is for accepting Cookies
driver.find_element(By.ID, 'ez-accept-all').click()

driver.find_element(By.NAME, 'firstname').send_keys('Georgian')
driver.find_element(By.NAME, 'lastname').send_keys('Popa')
driver.find_element(By.NAME, 'profession').click()


# find_element(By.LINK_TEXT)

driver.get(url)
# this is for accepting Cookies
driver.find_element(By.ID, 'ez-accept-all').click()

driver.find_element(By.LINK_TEXT, 'Top 7 Web Development Trends').click()
driver.find_element(By.LINK_TEXT, 'How I learned Selenium in 4 weeks').click()
driver.find_element(By.LINK_TEXT, 'A Complete Guide to API Development').click()


# find_element(By.PARTIAL_LINK_TEXT)

driver.get(url)
# this is for accepting Cookies
driver.find_element(By.ID, 'ez-accept-all').click()

driver.find_element(By.PARTIAL_LINK_TEXT ,'Development Trends').click()
driver.find_element(By.PARTIAL_LINK_TEXT ,'learned Selenium').click()
driver.find_element(By.PARTIAL_LINK_TEXT ,'API Development').click()


# find_element(By.TAG_NAME)

driver.get(url)
# this is for accepting Cookies
driver.find_element(By.ID, 'ez-accept-all').click()

tags_list = driver.find_elements(By.TAG_NAME,'input')

tags_list[0].send_keys('Georgian')
tags_list[1].send_keys('Popa')
tags_list[2].click()

# find_element(By.CLASS_NAME)

driver.get(url1)

class_list = driver.find_elements(By.CLASS_NAME,'form-control')

class_list[0].send_keys('Georgian')
class_list[1].send_keys('Popa')
class_list[2].send_keys('QA')
class_list[3].click()



# find element By.CLASS_NAME

driver.get(url1)

driver.find_element(By.CSS_SELECTOR,'#first-name').send_keys('Geo') # by ID
driver.find_element(By.CSS_SELECTOR,'.form-control').send_keys('Geo') # by class
driver.find_element(By.CSS_SELECTOR,'[placeholder="Enter your job title"]').send_keys('QA') # by attribute=value
driver.find_element(By.CSS_SELECTOR,'*[placeholder*="first name"]').send_keys('Geo) # by attribute=partial_value


'''Find element By.XPATH'''

driver.get(url1)

# by attribute=value

driver.find_element(By.XPATH, '//input[@id="first-name"]').send_keys('Georgian')
driver.find_element(By.XPATH, '//input[@id="last-name"]').send_keys('Popa')
driver.find_element(By.XPATH, '//input[@id="job-title"]').send_keys('QA')

# * all elements that comply with the rule

driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys('Geo')


select elements from the list

driver.find_element(By.XPATH, '(//input[@class="form-control"])[1]').send_keys('Geo')


# with OR, using pipe |

driver.find_element(By.XPATH, '//input[@id="first-name"] | //input[@id="last-name"]').send_keys('Geo')


# partial text link

text = driver.find_element(By.XPATH, '//a[contains(text(), "Submit")]').text
print(text)

# text link

driver.find_element(By.XPATH, '//a[text()="Submit"]').click()


#  with list of xpath and in python it ends up 1 element, so with (xpath)[1]

list = driver.find_elements(By.XPATH,"//input[@class='form-control']")
list[1].send_keys("Geo")
print(len(list))


# use parent::

driver.find_element(By.XPATH,"//div[@class='form-group']/parent::form/div/div[4]/div[2]/input").click()
driver.find_element(By.XPATH,"//div[@class='form-group']/parent::form/div/div[4]/div[3]/input").click()
driver.find_element(By.XPATH,"//div[@class='form-group']/parent::form/div/div[4]/div[4]/input").click()


# use the brother

driver.find_element(By.XPATH,
 "//div/form//div[@class='form-group']//strong/following-sibling::input[@placeholder='Enter your job title']").send_keys('QA')


# using function

# input_by_label
def input_by_label(label, input):
    my_input = driver.find_element(By.XPATH, f'//label[text()="{label}"]/parent::strong/parent::div//input')
    my_input.send_keys(input)


input_by_label('First name', 'Alain')
input_by_label('Last name', 'Delone')



# input_by_placeholder

def input_by_placeholder(placeholder, input):
    my_input = driver.find_element(By.XPATH,f'//input[@placeholder="{placeholder}"]')
    my_input.send_keys(input)

input_by_placeholder('Enter your job title', 'QA')




