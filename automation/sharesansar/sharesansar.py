from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.sharesansar.com/existing-issues")\

table_element = driver.find_element(By.ID, 'myTableEip')

row_elements = table_element.find_elements(By.TAG_NAME, 'tr')

for row in row_elements[1:]:
    data_elements = row.find_elements(By.TAG_NAME, 'td')
    for data in data_elements:
        print(data.text)


time.sleep(50)

driver.close()