from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/execute_script.html"

    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    # получить текст элемента
    x = x_element.text
    y = calc(x)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    robotCheckbox = browser.find_element_by_id("robotCheckbox")
    robotCheckbox.click()

    robotsRule = browser.find_element_by_id("robotsRule")
    robotsRule.click()

    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
