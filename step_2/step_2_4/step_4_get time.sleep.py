from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait1.html")

time.sleep(5)  #прога тормозит на 5 сек до клика на кнопку

button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")

assert message.text == "Verification was successful!"  #проверка того, что текст "Verification was successful!"

time.sleep(7)
browser.quit()