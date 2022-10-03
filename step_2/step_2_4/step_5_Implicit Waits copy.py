from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/wait1.html")

button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")

try:
    assert "successful" in message.text
    print("Слово successful есть при клике на кнопку!")
except AssertionError:
    print("Слова successful нет при клике на кнопку!")
