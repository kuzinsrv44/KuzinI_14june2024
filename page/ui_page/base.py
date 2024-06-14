import os
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base():

    def __init__(self):
        # Указываем путь к драйверу браузера (например, для Chrome)
        if os.name == 'nt':  # Windows
            driver_path = 'driver/chromedriver.exe'
        else:  # Linux or other OS
            driver_path = 'driver/chromedriver'
        self.service = Service(driver_path)
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        # Закрываем браузер после завершения теста
        with allure.step('Закрываем браузер'):
            self.driver.quit()

    def open_url(self, url):
        # Открываем страницу по указанному URL
        with allure.step('Открываем страницу'):
            return self.driver.get(url)

    def find_element(self, by, value):
        with allure.step('Ищем элемент'):
            try:
                element = self.driver.find_element(by, value)
                return element
            except:
                return None

    def is_element_present(self, by, value):
        with allure.step('Проверяем наличие элемента'):
            element = self.find_element(by, value)
            return element is not None

    def wait_for_element(self, by, value):
        # Ждем появления элемента на странице
        with allure.step('Выплняем ожидания появления элемента'):
            return self.wait.until(EC.presence_of_element_located((by, value)))

    def click_element(self, by, value):
        # Кликаем на элемент
        element = self.wait_for_element(by, value)
        element.click()

    def enter_text(self, by, value, text):
        # Вводим текст в поле
        with allure.step('Вводим текст в поле'):
            element = self.wait_for_element(by, value)
            element.clear()
            element.send_keys(text)

    def get_element_value(self, by, value):
        # Получаем значение элемента (например, текст элемента)
        with allure.step('Получаем значение элемента'):
            element = self.wait_for_element(by, value)
            return element.text

    def scroll(self):
        # Используем JavaScript для прокрутки до элемента
        with allure.step('Прокручиваем страницу'):
            self.driver.execute_script("window.scrollBy(0, 1000);")
