from re import X
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.CSS_SELECTOR, '.btn-primary').click()

alert = browser.switch_to.alert
alert.accept()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


number = browser.find_element(By.CSS_SELECTOR, '#input_value').text
print(type(number))

n = str(number)
y = calc(n)
print(y)

input = browser.find_element(By.CSS_SELECTOR, '[name="text"]').send_keys(y)

button_2 = browser.find_element(By.CSS_SELECTOR, '.btn-primary').click()

time.sleep(5)
browser.quit()