import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math



@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
class TestTime():
        def test_answer(self, browser, number):
            link = f"https://stepik.org/lesson/{number}/step/1"
            browser.get(link)
            browser.implicitly_wait(5)
            answer = math.log(int(time.time()+ 0.6))
            input1 = browser.find_element(By.TAG_NAME, "textarea")
            input1.send_keys(str(answer))
            button = browser.find_element(By.CLASS_NAME, "submit-submission")
            button.click()
            correction = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
            print("\n", correction.text)
            assert correction.text == "Correct!", f"ОР: 'Corrert!', ФР: '{correction.text}'"


