from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд


    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'h5#price'), '$100'))
    button = browser.find_element(By.ID, "book")
    button.click()

    x_element = browser.find_element(By.CSS_SELECTOR, "span#input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, "input#answer")
    input1.send_keys(y)

    button = browser.find_element(By.ID, "solve")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
