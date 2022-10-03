from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

button = browser.find_element(By.TAG_NAME, "button")
#browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#button.click() #тоже скролл

browser.execute_script(
    "window.scrollBy(0, 100);")  #команда проскролит страницу на 100px
button.click()

#button = document.getElementsByTagName("button")[0];
#button.scrollIntoView(true); #скролл джс

#with webdriver.Chrome() as browser:
#link = "https://SunInJuly.github.io/execute_script.html"
#browser.get(link)
#button = browser.find_element(By.TAG_NAME, "button")
#  _ = button.location_once_scrolled_into_view
# button.click()

#browser.execute_script("return arguments[0].scrollIntoView(true);", button) --- прокручивает вниз
#browser.execute_script("return arguments[0].scrollIntoView(false);", button) --- прокручивает вверх