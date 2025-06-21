import pickle

from selenium.common import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from faker import Faker
from selenium.webdriver.support.ui import Select
from meta_classes.meta_locators import MetaLocator
import time
import allure

class UIHelper(metaclass=MetaLocator):

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, timeout=15, poll_frequency=1)
        self.EC = EC
        self.actions = ActionChains(self.driver)
        self.fake = Faker()



    def find(self, locator: tuple, wait=False):
        if wait:
            return self.wait.until(self.EC.visibility_of_element_located(locator))
        else:
            return self.driver.find_element(*locator)


    def find_all(self, locator: tuple, wait=False):
        if wait:
            return self.wait.until(self.EC.visibility_of_all_elements_located(locator))
        else:
            return self.driver.find_elements(*locator)

    def fill(self, locator: tuple, text: str, clear: bool = False, wait = False):
        """
        Вводит текст в поле.
        :param wait: wait
        :param locator: Кортеж (метод локатора, значение)
        :param text: Текст для ввода
        :param clear: Очищать ли перед вводом (по умолчанию False)
        :return: Найденный элемент
        """
        element = self.find(locator, wait = False)
        if clear:
            element.clear()
        element.send_keys(text)
        return element  # Теперь `fill` возвращает элемент



    def click(self, locator: tuple, element_name: str=None):
        """
        This method makes click by element
        :param locator: XPATH
        :param element_name: Name for timeout exception
        :return:
        """
        self.wait.until(self.EC.element_to_be_clickable(locator), message=f"{element_name} is not clickable").click()


    def screenshot(self, name=time.time()):
        allure.attach(
            body = self.driver.get_screenshot_as_png(),
            name = name,
            attachment_type=allure.attachment_type.PNG
        )

    def wait_for_invisibility(self, locator: tuple, message: str=None):
        self.wait.until(self.EC.invisibility_of_element(locator), message=message)

    def wait_for_visibility(self, locator: tuple, message: str=None):
        self.wait.until(self.EC.visibility_of_element_located(locator), message=message)

    def wait_for_text_in_web_element(self, element, text: str, message: str = None):
        """
        Ожидает появления указанного текста в переданном WebElement.

        :param element: Веб-элемент, в котором ожидается текст.
        :param text: Ожидаемый текст.
        :param message: Дополнительное сообщение для исключения в случае таймаута (необязательно).
        :return: Исходный элемент, если текст найден.
        :raises TimeoutException: Если текст не появился в течение времени ожидания.
        """
        try:
            self.wait.until(lambda driver: text in element.text)
            return element
        except Exception as e:
            if message:
                raise TimeoutException(message)
            raise e

    def save_cookies(self, cookies_name="temp-cookies"):
        pickle.dump(self.driver.get_cookies(), open(f"cookies/{cookies_name}.pkl", "wb"))

    def load_cookies(self, cookies_name="temp-cookies"):
        cookies = pickle.load(open(f"cookies/{cookies_name}.pkl", "rb"))
        self.driver.delete_all_cookies()
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()

    def scroll_by(self, x, y):
        self.driver.execute_script(f"window.scrollTo({x}, {y})")

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0)")

    def scroll_to_element(self, locator):
        self.actions.scroll_to_element(self.find(locator))
        self.driver.execute_script("""
        window.scrollTo({
            top: window.scrollY + 500,
        });
        """)

    def select(self, locator: tuple, value: str):
        """
        Выбирает значение в выпадающем списке.
        :param locator: Кортеж (стратегия локатора, селектор)
        :param value: Текст или значение, которое нужно выбрать
        """
        element = self.find(locator)  # Находим элемент
        select = Select(element)  # Преобразуем его в Select
        try:
            select.select_by_visible_text(value)  # Выбираем по видимому тексту
        except:
            select.select_by_value(value)  # Если не получилось, пробуем по value



