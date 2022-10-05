from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get(
    "https://www.wildberries.by/catalog/38947926/detail.aspx?targetUrl=MI")
time.sleep(5)
button1 = browser.find_element(
    By.CSS_SELECTOR,
    ".sizes-list__item:nth-child(3) .sizes-list__size").click()
#button1.click()
time.sleep(5)
button2 = browser.find_element(
    By.CSS_SELECTOR,
    ".product-page__order-container > .order .hide-mobile").click()
time.sleep(5)
#button2.click()
#time.sleep(5)
browser.quit()
