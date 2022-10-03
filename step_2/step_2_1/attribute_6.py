from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    elements = browser.find_element(By.ID, "answer")

    #input1 = browser.find_element(By.ID, "answer").send_keys("Russia")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

#def calc(x):
#return str(math.log(abs(12 * math.sin(int(x)))))

#print(calc(642))
