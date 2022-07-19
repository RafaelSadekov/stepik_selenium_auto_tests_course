from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math



link = "https://stepik.org/lesson/236895/step/1"
try:
    browser = webdriver.Chrome()

    browser.get(link)
    browser.implicitly_wait(10)
    answer = math.log(int(time.time()))
    input1 = browser.find_element(By.TAG_NAME, "textarea")
    input1.send_keys(str(answer))
    button = browser.find_element(By.CLASS_NAME, "submit-submission")
    button.click()
    correction = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
    print(correction.text)
    assert correction.text == "Correct!", f"ОР: 'Corrert!', ФР: '{correction.text}'"

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()



