from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


link = 'http://suninjuly.github.io/execute_script.html'
browser = webdriver.Chrome()
browser.get(link)

num1 = browser.find_element(By.ID, "input_value").text
x = int(num1)
print(x)

button = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

input = browser.find_element(By.CSS_SELECTOR,
                             ".form-control").send_keys(calc(x))

checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
radiobutton = browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()

button = browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()

time.sleep(5)
# закрываем браузер после всех манипуляций
browser.quit()
