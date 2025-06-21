from selenium.common import StaleElementReferenceException

from base.base_page import BasePage
from config.credential import Credential




class Create(BasePage):



    _DROPDOWN_LOCATOR = "//span[@aria-describedby='Role']//span[@class='e-input-group-icon e-ddl-icon e-search-icon']"
    _ROLES_LOCATOR = "//li[@role='option']"

    _LOGIN_FIELD_LOCATOR = "//input[@id='Login']"
    _PASSWORD_FIELD_LOCATOR = "//input[@id='Password']"
    _COMMENTS_FIELD_LOCATOR = "//textarea[@id='Comment']"

    _BUTTON_CREATE_LOCATOR = "//button[text()='Create']"


    def fill_market_type(self, market_type):
        self.ui_helper.click(self._DROPDOWN_LOCATOR)
        for _ in range(3):  # максимум 3 попытки
            try:
                elements = self.ui_helper.find_all(self._ROLES_LOCATOR, wait=True)
                for element in elements:
                    if market_type in element.text:
                        element.click()
                        return  # если клик удался, выходим из метода
            except StaleElementReferenceException:
                continue  # если элемент устарел, пробуем заново
        raise Exception(f"Failed to select market type '{market_type}' after 3 attempts.")


    def fill_login(self):
        self.ui_helper.fill(self._LOGIN_FIELD_LOCATOR, Credential.MANAGER_LOGIN, clear=True)

    def fill_password(self):
        self.ui_helper.fill(self._PASSWORD_FIELD_LOCATOR, Credential.MANAGER_PASSWORD, clear=True)

    def fill_comments(self, text):
        self.ui_helper.fill(self._COMMENTS_FIELD_LOCATOR, text, clear=True)

    def click_create(self):
        self.ui_helper.click(self._BUTTON_CREATE_LOCATOR)



