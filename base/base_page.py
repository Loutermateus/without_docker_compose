from meta_classes.meta_locators import MetaLocator
from helpers.ui_helper import UIHelper
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



class BasePage(metaclass=MetaLocator):


    def __init__(self, driver):
        self.driver = driver
        self.ui_helper = UIHelper(self.driver)
        self.wait = WebDriverWait(self.driver,timeout=15,poll_frequency=1)
        self.EC = EC






    def open(self):
        self.driver.get(self._PAGE_URL)

    def is_open(self):
        self.wait.until(self.EC.url_to_be(self._PAGE_URL))

    def refresh_page(self):
        self.driver.refresh()










