
import unittest
from selenium import webdriver
import time


class TestRegistration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome()

    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.__script(link)

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.__script(link)

    def __script(self, link):

        self.browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = self.browser.find_element_by_css_selector(".first_block .first")
        input1.send_keys("Ivan")
        input2 = self.browser.find_element_by_css_selector(".first_block .second")
        input2.send_keys("Petrov")
        input3 = self.browser.find_element_by_css_selector(".first_block .third")
        input3.send_keys("test@mail.ru")

        # Отправляем заполненную форму
        button = self.browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = self.browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


if __name__ == "__main__":
    unittest.main()


