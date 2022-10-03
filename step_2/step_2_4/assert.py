from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/wait1.html")

button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")
print("Смотрим тип переменной message", type(message))
print("Смотрим тип после преобразование к типу строка переменной message",
      type(message.text))

try:
    assert "successful" in message.text
    print("Тест assert 'successful' in 'message.text' успешно выполнен!")
    print(
        "Слово successful есть в сообщении об успешной проверке вывода текста Verification was successful!"
    )
except AssertionError:
    print("Тест assert 'successful' in 'message.text' НЕ выполнен...")
    print(
        "Слово successful НЕТ в сообщении об успешной проверке вывода текста Verification was successful..."
    )
