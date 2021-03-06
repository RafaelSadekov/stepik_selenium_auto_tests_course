from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time


try:
    browser = webdriver.Chrome()

    browser.execute_script("alert('Robots at work');")
    #Переход на новую вкладку браузера
#При работе с веб-приложениями приходится переходить по ссылкам, которые открываются в новой вкладке браузера.
# WebDriver может работать только с одной вкладкой браузера. При открытии новой вкладки WebDriver продолжит работать со старой вкладкой.
# Для переключения на новую вкладку надо явно указать, на какую вкладку мы хотим перейти. Это делается с помощью команды switch_to.window:

browser.switch_to.window(window_name)
#Чтобы узнать имя новой вкладки, нужно использовать метод window_handles, который возвращает массив имён всех вкладок.
# Зная, что в браузере теперь открыто две вкладки, выбираем вторую вкладку:

new_window = browser.window_handles[1]
#Также мы можем запомнить имя текущей вкладки, чтобы иметь возможность потом к ней вернуться:

first_window = browser.window_handles[0]
#После переключения на новую вкладку поиск и взаимодействие с элементами будут происходить уже на новой странице.



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
