from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random,string

## python -c 'import selenium_tests; selenium_tests.registerRandomTest()'
## python -c 'import selenium_tests; selenium_tests.loginRegisteredUserTest()'
## python -c 'import selenium_tests; selenium_tests.emailFormFixTest()'
## python -c 'import selenium_tests; selenium_tests.websiteFormFixTest()'
## python -c 'import selenium_tests; selenium_tests.instagramLoginTest()'


##driver = webdriver.Chrome('/Users/Eric/Documents/chromedriver')
driver = webdriver.Firefox()
driver.get('http://127.0.0.1:8000/home/')



## REGISTER NEW USER
def registerRandomTest():

    driver.find_element_by_link_text("Register").click()
    driver.find_element_by_id('id_username').send_keys(''.join(random.choice(string.lowercase) for i in range(10)))
    driver.find_element_by_id('id_email').send_keys("eric.assaly@gmail.com")
    driver.find_element_by_id('id_password').send_keys("welcome")
    driver.find_element_by_id('id_website').send_keys("http://www.google.ca")
    driver.find_element_by_name('submit').click()
    element = driver.find_element_by_xpath('/html/body/strong')
    print element.text
    assert element.text == "Thank you for registering with Touristy!"
    driver.quit()

## LOGIN WITH REGISTERED USER
def loginRegisteredUserTest():
    driver.find_element_by_link_text("Login").click()
    driver.find_element_by_name('username').send_keys("eric")
    driver.find_element_by_name('password').send_keys("a")
    submit_button = driver.find_element_by_css_selector('input[type="submit"]')
    submit_button.click()
    element = driver.find_element_by_xpath('//*[@id="top-div"]/h1')
    assert element.text == "Hello eric, welcome back to Touristy!"
    driver.quit()


## REGISTER WITH TAKEN USERNAME
def registerTakenTest():
    driver.find_element_by_link_text("Register").click()

    driver.find_element_by_id('id_username').send_keys('eric')
    driver.find_element_by_id('id_email').send_keys("eric.assaly@gmail.com")
    driver.find_element_by_id('id_password').send_keys("welcome")
    driver.find_element_by_id('id_website').send_keys("http://www.google.ca")

    driver.find_element_by_name('submit').click()
    element = driver.find_element_by_xpath('//*[@id="user_form"]/ul/li')
    print element.text
    assert element.text == "User with this Username already exists."
    driver.quit()


##EMAIL MISFORMATTED & FIXED AFTER
def emailFormFixTest():
    driver.find_element_by_link_text("Register").click()
    text_area = driver.find_element_by_id('id_username')
    text_area.send_keys(''.join(random.choice(string.lowercase) for i in range(10)))
    text_area = driver.find_element_by_id('id_email')
    text_area.send_keys("eric@gmail")
    text_area = driver.find_element_by_id('id_password')
    text_area.send_keys("welcome")
    text_area = driver.find_element_by_id('id_website')
    text_area.send_keys("http://www.google.ca")
    submit_button = driver.find_element_by_name('submit')
    submit_button.click()
    element = driver.find_element_by_xpath('//*[@id="user_form"]/ul/li')
    print element.text
    assert element.text == "Enter a valid email address."
    driver.find_element_by_id('id_email').clear()
    text_area = driver.find_element_by_id('id_email')
    text_area.send_keys("eric@gmail.com")
    text_area = driver.find_element_by_id('id_password')
    text_area.send_keys("welcome")
    submit_button = driver.find_element_by_name('submit')
    submit_button.click()
    element = driver.find_element_by_xpath('/html/body/strong')
    print element.text
    assert element.text == "Thank you for registering with Touristy!"
    driver.quit()

def websiteFormFixTest():
    driver.find_element_by_link_text("Register").click()

    randomString1 = ''.join(random.choice(string.lowercase) for i in range(5))
    randomString2 = ''.join(random.choice(string.lowercase) for i in range(5))

    driver.find_element_by_id('id_username').send_keys(randomString1.join(' ').join(randomString2))
    driver.find_element_by_id('id_email').send_keys("eric@gmail.com")
    driver.find_element_by_id('id_password').send_keys("welcome")
    driver.find_element_by_id('id_website').send_keys("http://www.google.ca")
    driver.find_element_by_name('submit').click()
    element = driver.find_element_by_xpath('//*[@id="user_form"]/ul/li')
    print element.text
    assert element.text == "Enter a valid username."
    driver.find_element_by_id('id_username').clear()
    driver.find_element_by_id('id_username').send_keys(randomString1.join(randomString2))
    driver.find_element_by_id('id_password').send_keys("welcome")
    driver.find_element_by_name('submit').click()
    element = driver.find_element_by_xpath('/html/body/strong')
    print element.text
    assert element.text == "Thank you for registering with Touristy!"
    driver.quit()

##LOGIN TO INSTAGRAM

def instagramLoginTest():
    driver.find_element_by_link_text("Login").click()
    driver.find_element_by_name('username').send_keys('eric')
    driver.find_element_by_name('password').send_keys('a')
    driver.find_element_by_css_selector('input[type="submit"]').click()


    driver.find_element_by_link_text("Login to Instagram").click()

    print driver.title,' is the title'
    assert "Instagram" in driver.title

    driver.find_element_by_id('id_username').send_keys('3r1c0')
    driver.find_element_by_id('id_password').send_keys('yapper1200')
    driver.find_element_by_css_selector('input.button-green').submit()

    print driver.title
    assert "Touristy" in driver.title

    driver.find_element_by_id('pac-input').send_keys('Bridges Restaurant, Duranleau Street, Vancouver, BC, Canada')
    driver.find_element_by_id('pac-input').send_keys(Keys.ENTER)
    driver.quit()


# ##LOGIN, SEARCH, APPEAR IN HISTORY (assume logged into instagram)
def historyTest():
    driver.find_element_by_link_text("Login").click()
    driver.find_element_by_name('username').send_keys('eric')
    driver.find_element_by_name('password').send_keys('a')
    driver.find_element_by_css_selector('input[type="submit"]').click()


    driver.find_element_by_link_text("Login to Instagram").click()
    driver.find_element_by_id('id_username').send_keys('3r1c0')
    driver.find_element_by_id('id_password').send_keys('yapper1200')
    driver.find_element_by_css_selector('input.button-green').submit()

    driver.find_element_by_id('pac-input').send_keys('Bridges Restaurant, Duranleau Street, Vancouver, BC, Canada')
    driver.find_element_by_id('pac-input').send_keys(Keys.ENTER)


    driver.find_element_by_xpath('//div[@id="map-canvas"]/div/div/div[2]').submit()
    driver.find_element_by_css_selector('button').submit()

    element = driver.find_element_by_xpath('//*[@id="instagram"]/p/text()[1]')
    print element
    assert element.text == "Stanley Park"








