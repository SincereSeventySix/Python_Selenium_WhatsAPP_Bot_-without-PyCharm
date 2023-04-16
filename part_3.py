from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
driver_service = Service(executable_path="C:/Program Files (x86)/chromedrive.exe")
from selenium.webdriver.common.keys import Keys

# More functions from the selenium library to help us locate the person(s) we want to message.

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:/Users/acer/AppData/Local/Google/Chrome/User Data")
driver = webdriver.Chrome(service=driver_service)
driver.get("https://web.whatsapp.com/")
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 30)

FTRR='"R Astley"' #must be stroed as string to be later executed as string hence single quotes outside of double quotes
#FTRR means friends to rick roll

#Syntax for using Xpath = '//TAGNAME[contains(@ATTRIBUTE, ' + target +')]'

FTRR_path ='//span[contains(@title,' + FTRR +')]'
contact=wait.until(EC.presence_of_element_located((By.XPATH,FTRR_path)))
contact.click()

sleep(3)
input("We're in!")





