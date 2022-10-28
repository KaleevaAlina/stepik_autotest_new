import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(
            By.CSS_SELECTOR,
            ".first_block > .first_class > .form-control").send_keys("Алинэ")
        time.sleep(3)
        input2 = browser.find_element(
            By.CSS_SELECTOR,
            ".first_block > .second_class > .form-control").send_keys(
            "Бэс оф зе бест")
        time.sleep(3)
        input3 = browser.find_element(
            By.CSS_SELECTOR,
            ".first_block > .third_class > .form-control").send_keys("Васильевна")
        time.sleep(3)

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        assert "Congratulations! You have successfully registered!" == welcome_text_elt, "Провал"

        time.sleep(10)
        browser.quit()


if __name__ == "__main__":
    unittest.main()
