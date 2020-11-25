from selenium import webdriver
from time import sleep
from Excel_read import xlsxreader
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.facebook.com/')
print ("Opened facebook")
sleep(1)
driver.get('https://www.facebook.com/')
print("Finished")
