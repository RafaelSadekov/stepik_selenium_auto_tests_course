from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

link = "http://suninjuly.github.io/registration1.html"

class TestAbs(unittest.TestCase):
    def test_reg(self):
        browser = webdriver.Chrome()
        browser.get(link)


        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.XPATH, "//input[@class='form-control first' and @required]")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, "//input[@class='form-control second' and @required]")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, "//input[@class='form-control third' and @required]")
        input3.send_keys("petrov@gmail.com")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
        time.sleep(1)

    # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Должно быть написано: Congratulations! You have successfully registered!")

    # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
    # закрываем браузер после всех манипуляций
        browser.quit()

if __name__ == "__main__":
    unittest.main()


