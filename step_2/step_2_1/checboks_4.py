from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x_element = browser.find_element(By.CSS_SELECTOR,
                                 "form>div>label>span#input_value")
x = x_element.text
time.sleep(1)
print(x)
y = calc(x)
time.sleep(1)
print(y)
elements = browser.find_element(By.ID, "answer").send_keys(y)
time.sleep(1)
elements = browser.find_element(By.ID, "robotCheckbox").click()
option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']").click()

time.sleep(1)
# Отправляем заполненную форму
button = browser.find_element(By.CSS_SELECTOR, ".btn").click()

# ждем загрузки страницы
time.sleep(1)

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(4)
# закрываем браузер после всех манипуляций
browser.quit()