from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/math.html"

    browser.get(link)

    people_radio = browser.find_element_by_id("peopleRule")

    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    # проверка 1-м стособом
    assert people_checked is not None, "People radio is not selected by default"

    # проверка 2-м стособом
    assert people_checked == "true", "People radio is not selected by default"

    robots_radio = browser.find_element_by_id("robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    print("value of robots radio: ", robots_checked)
    assert robots_checked is None

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
