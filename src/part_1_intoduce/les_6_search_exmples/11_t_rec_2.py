from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    i1 = browser.find_element_by_css_selector('div.first_block > div.first_class > input.first')
    i1.send_keys('f1')

    i2 = browser.find_element_by_css_selector('div.first_block > div.second_class > input.second')
    i2.send_keys('f2')

    i3 = browser.find_element_by_css_selector('div.first_block > div.third_class > input.third')
    i3.send_keys('f3')

    i4 = browser.find_element_by_css_selector('div.second_block > div.first_class > input.first')
    i4.send_keys('f4')

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()