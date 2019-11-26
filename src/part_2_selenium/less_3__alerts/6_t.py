from selenium import webdriver
import math
import time

# Открыть страницу http://suninjuly.github.io/redirect_accept.html
# Нажать на кнопку
# Переключиться на новую вкладку
# Пройти капчу для робота и получить число-ответ

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()

try:
    # Открыть страницу http://suninjuly.github.io/redirect_accept.html
    link = " http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    # Нажать на кнопку
    button = browser.find_element_by_tag_name("button")
    button.click()

    # time.sleep(1)

    # Переключиться на новую
    window_name = browser.window_handles[1]
    browser.switch_to.window(window_name)

    # На новой странице решить капчу для роботов, чтобы получить число с ответом
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
