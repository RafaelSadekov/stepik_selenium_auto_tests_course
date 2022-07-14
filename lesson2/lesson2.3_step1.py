from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time


try:
    browser = webdriver.Chrome()

    browser.execute_script("alert('Robots at work');")
    alert = browser.switch_to.alert
    alert.accept()

#Для confirm-окон
confirm = browser.switch_to.alert
confirm.accept()
confirm.dismiss()

#модального окна prompt
prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
