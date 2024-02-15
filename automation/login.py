from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

input_element = driver.find_element(By.ID, 'username')
input_element.send_keys("tomsmith")

input_element2 = driver.find_element(By.ID, 'password')
input_element2.send_keys("SuperSecretPassword!")

login = driver.find_element(By.CLASS_NAME, 'radius')
login.send_keys(Keys.RETURN)

message_element = driver.find_element(By.CLASS_NAME, 'subheader')
print(message_element.text)


time.sleep(50)

driver.close()
