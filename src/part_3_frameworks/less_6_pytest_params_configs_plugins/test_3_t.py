import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import math

# pytest -s -v test_3_t.py

# answer: The owls are not what they seem! OvO


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link_id', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, link_id):
    link = f"https://stepik.org/lesson/{link_id}/step/1"
    browser.get(link)

    answer_input = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".ember-text-area"))
    )

    answer = math.log(int(time.time()))
    answer_input.send_keys(str(answer))

    browser.find_element_by_css_selector(".submit-submission").click()

    hint_div = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".smart-hints__hint"))
    )

    text = hint_div.text

    correct_text = "Correct!"
    assert text == correct_text, f"text should be \"{correct_text}\", get \"{text}\""
