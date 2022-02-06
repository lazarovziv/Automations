import argparse

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
args = parser.parse_args()

if args.browser:
    if args.browser == 'chrome' or args.browser == 'Chrome':
        driver = webdriver.Chrome()
    elif args.browser == 'safari' or args.browser == 'Safari':
        driver = webdriver.Safari()
    elif args.browser == 'firefox' or args.browser == 'Firefox' or args.browser == 'FireFox':
        driver = webdriver.Firefox()
    elif args.browser == 'edge' or args.browser == 'Edge':
        driver = webdriver.Edge()
else:
    print('Please choose a browser!')
    quit()

# TODO: add validation check for credentials
if not args.id or not args.username or not args.password:
    print('Please enter a username, password and id credentials.')
    quit()

print(f"Opening {args.browser.title()}...")

# driver = webdriver.Safari()
driver.get('https://www.openu.ac.il')
login_form_button_element = driver.find_element(By.ID, 'openu_myop_plugin_MyOpAppsBtn')
login_form_button_element.click()

iframe = driver.find_element(By.XPATH, "//*[@id='openu_myop_plugin_apps_iframeId']")
driver.switch_to.frame(iframe)

username = WebDriverWait(driver, timeout=7).until(
    EC.presence_of_element_located(
        (By.XPATH, "//fieldset//input[@id='p_user']")
    )
)
password = WebDriverWait(driver, timeout=2).until(
    EC.presence_of_element_located(
        (By.XPATH, "//fieldset//input[@id='p_sisma']")
    )
)
id = WebDriverWait(driver, timeout=2).until(
    EC.presence_of_element_located(
        (By.XPATH, "//fieldset//input[@id='p_mis_student']")
    )
)

username.send_keys(args.username)
password.send_keys(args.password)
id.send_keys(args.id)

id.send_keys(Keys.RETURN)