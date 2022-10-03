from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

link = 'http://suninjuly.github.io/selects2.html'
browser = webdriver.Chrome()
browser.get(link)

select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value("1")  # ищем элемент с текстом "Python"

#select.select_by_visible_text("text")
#select.select_by_index(index)
#select.select_by_visible_text("Python")
#select.select_by_index(1)
