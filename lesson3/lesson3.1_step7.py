actual_result = -42
assert abs(-42) == actual_result , 'Wrong result, got ' + str(actual_result) + ', smth wrong'

catalog_text = self.catalog_link.text # считываем текст и записываем его в переменную
assert catalog_text == "Каталог", \
    f"Wrong language, got {catalog_text} instead of 'Каталог'"
