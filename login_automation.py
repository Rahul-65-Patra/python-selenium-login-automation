from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import random
import string

driver = webdriver.Chrome()

driver.get("http://127.0.0.1:8000/login")

time.sleep(2)

email = ''.join(random.choices(string.ascii_lowercase, k=6)) + "@gmail.com"
password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

driver.find_element(By.ID, "email").send_keys(email)
driver.find_element(By.ID, "password").send_keys(password)


time.sleep(10)
driver.quit()
