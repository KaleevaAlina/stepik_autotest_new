import time
from selenium import webdriver
from selenium.webdriver.common.by import By
with webdriver.Chrome() as browser:
    result = []
    browser.get('http://parsinger.ru/blank/2/1.html')
    time.sleep(1)
    browser.execute_script(
        'window.open("http://parsinger.ru/blank/2/2.html", "_blank1");')
    browser.execute_script(
        'window.open("http://parsinger.ru/blank/2/3.html", "_blank2");')
    browser.execute_script(
        'window.open("http://parsinger.ru/blank/2/4.html", "_blank3");')

    time.sleep(1)
    for x in reversed(range(len(browser.window_handles))):
        browser.switch_to.window(browser.window_handles[x])
        for y in browser.find_elements(By.CLASS_NAME, 'check'):
            y.click()