from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.CSS_SELECTOR, '.btn-primary').click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


numberText = browser.find_element(By.CSS_SELECTOR, '#input_value').text
print(numberText)

print(calc(numberText))

input = browser.find_element(By.CSS_SELECTOR,
                             '#answer').send_keys(calc(numberText))

buttonSecond = browser.find_element(By.CSS_SELECTOR, '.btn-primary').click()
time.sleep(5)

alert = browser.switch_to.alert.accept()

time.sleep(7)
browser.quit()
