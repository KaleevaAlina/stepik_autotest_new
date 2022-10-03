from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

WebDriverWait(browser, "12").until(
    EC.text_to_be_present_in_element((By.ID, "price"), "100"))

button = browser.find_element(By.ID, "book").click()

browser.execute_script(
    "window.scrollBy(0, 400);")  #команда проскролит страницу на 100px


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
numberText = browser.find_element(By.CSS_SELECTOR, '#input_value').text
print(numberText)

print(calc(numberText))

input = browser.find_element(By.CSS_SELECTOR,
                             '#answer').send_keys(calc(numberText))

buttonSecond = browser.find_element(By.CSS_SELECTOR, '#solve').click()
