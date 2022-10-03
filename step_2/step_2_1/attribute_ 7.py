from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

get_img = browser.find_element(By.CSS_SELECTOR, 'img#treasure')

get_attribute = get_img.get_attribute('valuex')
print(get_attribute, 'Какое-то непонятное значение')

x = int(get_attribute)
y = calc(x)
print(y)

input = browser.find_element(By.ID, 'answer').send_keys(y)

checkbox = browser.find_element(By.ID, "robotCheckbox").click()
radiob = browser.find_element(By.ID, "robotsRule").click()
button = browser.find_element(By.CSS_SELECTOR, ".btn-default").click()

time.sleep(10)
browser.quit()