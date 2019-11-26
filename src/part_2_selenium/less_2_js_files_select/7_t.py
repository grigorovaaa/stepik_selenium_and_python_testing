from selenium import webdriver
import os
import time

browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/file_input.html"

    browser.get(link)

    input_firstname = browser.find_element_by_name("firstname")
    input_firstname.send_keys("Ivan")
    input_lastname = browser.find_element_by_name("lastname")
    input_lastname.send_keys("Petrov")
    input_email = browser.find_element_by_name("email")
    input_email.send_keys("test@mail.ru")

    input_file = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    input_file.send_keys(file_path)

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
