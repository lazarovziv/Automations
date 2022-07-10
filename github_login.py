import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

try:
    credentials_file_read = open(f"{os.getcwd()}/github_credentials.txt", 'r')
    lines = credentials_file_read.readlines()
    count = 0
    for line in lines:
        if count == 0:
            username = line.strip()
            count += 1
        else:
            password = line.strip()
except IOError:
    print('An IO error occurred')

url = 'https://github.com/login'

# using on macOS
driver = webdriver.Safari()
driver.get(url)

username_element = driver.find_element(By.ID, 'login_field')
password_element = driver.find_element(By.ID, 'password')

username_element.send_keys(str(username))
password_element.send_keys(str(password))
password_element.send_keys(Keys.RETURN)
