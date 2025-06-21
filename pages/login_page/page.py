from config.credential import Credential
from base.base_page import BasePage
from config.urls import Urls





class LoginPage(BasePage):



    _PAGE_URL = Urls.LOGiN_PAGE

    _LOGIN_FIELD_LOCATOR = "//input[@id='Login']"
    _PASSWORD_FIELD_LOCATOR = "//input[@id='Password']"
    _BUTTON_CLICK_LOCATOR = "//input[@value='Login']"

    def login(self):
        self.ui_helper.fill(self._LOGIN_FIELD_LOCATOR, Credential.LOGIN, clear=True)
        self.ui_helper.fill(self._PASSWORD_FIELD_LOCATOR, Credential.PASSWORD,  clear=True)
        self.ui_helper.click(self._BUTTON_CLICK_LOCATOR)


    def login_as(self, user_type):
        if user_type == "admin":
            self.ui_helper.fill(self._LOGIN_FIELD_LOCATOR, Credential.LOGIN, clear=True)
            self.ui_helper.fill(self._PASSWORD_FIELD_LOCATOR, Credential.PASSWORD, clear=True)
            self.ui_helper.click(self._BUTTON_CLICK_LOCATOR)
        elif user_type == "manager":
            self.ui_helper.fill(self._LOGIN_FIELD_LOCATOR, Credential.MANAGER_LOGIN, clear=True)
            self.ui_helper.fill(self._PASSWORD_FIELD_LOCATOR, Credential.MANAGER_PASSWORD, clear=True)
            self.ui_helper.click(self._BUTTON_CLICK_LOCATOR, "Login button")






