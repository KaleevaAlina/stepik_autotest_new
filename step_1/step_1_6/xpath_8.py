from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form")
    elements = browser.find_elements(By.CSS_SELECTOR, "[type=text]")
    for element in elements:
        element.send_keys("хуй")
    button = browser.find_element(
        By.XPATH, "/html/body/div/form/div[6]/button[3]").click()

finally:
    # успеваем скопировать код за 30 секунд

    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
