
#assert abs(-42) == 42, "Модуль числа"
# print("Принт")

# print("Let's count together: {}, then goes {}, and then {}".format(
#  "one", "two", "three")) - функция которая подставляет значения


#str1 = "one"
#str2 = "two"
#str3 = "three"
#print(f"Let's count together: {str1}, then goes {str2}, and then {str3}")

#actual_result = "abrakadabra"
#print(f"Wrong text, got {actual_result}, something wrong")


# catalog_text = self.catalog_link.text # считываем текст и записываем его в переменную
# assert catalog_text == "Каталог", \
#f"Wrong language, got {catalog_text} instead of 'Каталог'"

def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, f"expected {expected_result}, got {actual_result}"
