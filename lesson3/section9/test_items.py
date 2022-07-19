from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"



def test_single_add_to_basket_button_should_be_present(browser):
    browser.get(link)
    #time.sleep(20)
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "btn-add-to-basket")))
    add_to_basket_button_elements = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    assert len(add_to_basket_button_elements) == 1


