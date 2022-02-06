import argparse
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC

# TODO: add default browser based on OS used

parser = argparse.ArgumentParser(description='Choose a browser to use and specify your username, password and id. No data is being collected!')
parser.add_argument('-b', '--browser')
parser.add_argument('-i', '--id')
parser.add_argument('-u', '--username')
parser.add_argument('-p', '--password')
parser.add_argument('-s', '--print', action='store_true')
args = parser.parse_args()

# write to file
credentials_file_read = open(f"{os.getcwd()}/credentials.txt", 'r')
lines = credentials_file_read.readlines()
row_counter = 0
for line in lines:
    row_counter += 1
    if row_counter == 1:
        username = line.strip()
    elif row_counter == 2:
        password = line.strip()
    elif row_counter == 3:
        id = line.strip()
    elif row_counter == 4:
        browser = line.strip().lower()

if row_counter == 0 or args.username or args.password or args.id:
    # TODO: add validation check for credentials
    if not args.id or not args.username or not args.password:
        print('Please enter a username, password and id credentials.')
        quit()

    credentials_file_write = open('credentials.txt', 'w')
    credentials_file_write.write(f"{args.username}\n")
    credentials_file_write.write(f"{args.password}\n")
    credentials_file_write.write(f"{args.id}\n")
    credentials_file_write.write(f"{args.browser}\n")
    credentials_file_write.close()

    username = args.username
    password = args.password
    id = args.id
    browser = args.browser

# if user wants to print credentials to screen
if args.print:
    print(f"Username: {username}")
    print(f"Password: {password}")
    print(f"ID: {id}")

if browser:
    if browser == 'chrome' or browser == 'Chrome':
        driver = webdriver.Chrome()
    elif browser == 'safari' or browser == 'Safari':
        driver = webdriver.Safari()
    elif browser == 'firefox' or browser == 'Firefox' or browser == 'FireFox':
        driver = webdriver.Firefox()
    elif browser == 'edge' or browser == 'Edge':
        driver = webdriver.Edge()
    else:
        print('Please choose a valid browser! (Chrome, Safari, Firefox, Edge)')
        quit()    
else:
    print('Please choose a browser!')
    quit()

print(f"Opening {browser.title()}...")

driver.get('https://www.openu.ac.il')
login_form_button_element = driver.find_element(By.ID, 'openu_myop_plugin_MyOpAppsBtn')
login_form_button_element.click()

iframe = driver.find_element(By.XPATH, "//*[@id='openu_myop_plugin_apps_iframeId']")
driver.switch_to.frame(iframe)

username_element = WebDriverWait(driver, timeout=7).until(
    EC.presence_of_element_located(
        (By.XPATH, "//fieldset//input[@id='p_user']")
    )
)
password_element = WebDriverWait(driver, timeout=2).until(
    EC.presence_of_element_located(
        (By.XPATH, "//fieldset//input[@id='p_sisma']")
    )
)
id_element = WebDriverWait(driver, timeout=2).until(
    EC.presence_of_element_located(
        (By.XPATH, "//fieldset//input[@id='p_mis_student']")
    )
)

username_element.send_keys(str(username))
password_element.send_keys(str(password))
id_element.send_keys(str(id))

id_element.send_keys(Keys.RETURN)