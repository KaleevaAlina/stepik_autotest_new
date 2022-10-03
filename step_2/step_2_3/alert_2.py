from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element(By.CSS_SELECTOR, '[name = "firstname"]')
input1.send_keys("Alina")

input1 = browser.find_element(By.CSS_SELECTOR, '[name = "lastname"]')
input1.send_keys("Kaleeva")

input1 = browser.find_element(By.CSS_SELECTOR, '[name = "email"]')
input1.send_keys("Kaleeva.fam@gmail.com")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "text.txt"

# получаем путь к text.txt
file_path = os.path.join(current_dir, file_name)

#print(file_path)

inputText = browser.find_element(By.CSS_SELECTOR,
                                 '[name="file"]').send_keys(file_path)

button = browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()

alert = browser.switch_to.alert
alert.accept()

time.sleep(7)
browser.quit()
