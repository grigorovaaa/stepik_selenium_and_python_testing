from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/get_attribute.html"

    browser.get(link)

    chest = browser.find_element_by_id("treasure")
    # получить текст элемента
    x = chest.get_attribute("valuex")
    y = calc(x)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    robotCheckbox = browser.find_element_by_id("robotCheckbox")
    robotCheckbox.click()

    robotsRule = browser.find_element_by_id("robotsRule")
    robotsRule.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
