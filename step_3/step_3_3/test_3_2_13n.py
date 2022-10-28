import unittest
from selenium import webdriver
import time


class test_regisracia(unittest.TestCase):
    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        #link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля

        input1 = browser.find_element_by_css_selector(
            ".first_block > div.first_class input")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector(
            ".first_block > div.second_class input")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector(
            ".first_block > div.third_class input")
        input3.send_keys("nety@mail.ru")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!",
                         welcome_text, "Сравнение верно!")
        #assert "Congratulations! You have successfully registered!" == welcome_text

        time.sleep(5)
        browser.quit()

    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        #link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля

        input1 = browser.find_element_by_css_selector(
            ".first_block > div.first_class input")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector(
            ".first_block > div.second_class input")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector(
            ".first_block > div.third_class input")
        input3.send_keys("nety@mail.ru")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!",
                         welcome_text, "Сравнение верно!")
        #assert "Congratulations! You have successfully registered!" == welcome_text

        time.sleep(5)
        browser.quit()


if __name__ == "__main__":
    unittest.main()
