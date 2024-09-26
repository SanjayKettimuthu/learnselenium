from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.amazon.in")
astatus = driver.title
time.sleep(5)
driver.get("https://www.flipkart.com")
fstatus = driver.title
print("status from amazon and flipkart are :" +astatus+", " +fstatus)
time.sleep(5)
driver.quit()
