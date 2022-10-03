from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

link = 'http://suninjuly.github.io/selects1.html'
browser = webdriver.Chrome()
browser.get(link)

num1 = browser.find_element(By.ID, "num1").text
num2 = browser.find_element(By.ID, "num2").text
sum = int(num1) + int(num2)
print(sum, 'Значение')

select = Select(browser.find_element(By.ID, "dropdown"))
select.select_by_value(str(sum))  # ищем элемент с текстом "Python"
button = browser.find_element(By.CSS_SELECTOR, ".btn-default").click()

time.sleep(7)
browser.quit()