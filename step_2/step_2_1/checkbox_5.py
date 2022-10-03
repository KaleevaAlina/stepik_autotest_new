from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")

x = x_element.text
y = calc(x)
print("Вывожу значение", y)

x_element = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)

checkbox = browser.find_element(By.CSS_SELECTOR,
                                ".form-check #robotCheckbox").click()
checkbox = browser.find_element(By.CSS_SELECTOR,
                                ".form-check #robotsRule").click()
button = browser.find_element(By.CSS_SELECTOR, ".btn-default").click()

time.sleep(10)
browser.quit()