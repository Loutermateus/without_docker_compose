from base.base_page import BasePage
from base_components.menu.components.settings import Settings
from base_components.menu.components.databases import Databases
from base_components.menu.components.risk_management import RiskManagement
from base_components.menu.components.home import Home



class Menu(BasePage):



    _HOME_LOCATOR = "//li[@id='header_menuitem_home']"
    _OVERVIEW_LOCATOR = "//li[@id='header_menuitem_overview']"
    _MARKET_WATCH_LOCATOR = "//li[@id='header_menuitem_marketwatch']"
    _EXPOSURE_LOCATOR = "//li[@id='header_menuitem_exposure']"
    _USERS_LOCATOR = "//li[@id='header_menuitem_users']"
    _LOGOUT_LOCATOR = "//li[@id='header_menuitem_logout']"


    def __init__(self, driver):
        super().__init__(driver)
        self.settings = Settings(self.driver)
        self.databases = Databases(self.driver)
        self.risk_management = RiskManagement(self.driver)
        self.home = Home(self.driver)




    def open_home(self):
        self.ui_helper.click(self._HOME_LOCATOR, "Button home")

    def open_overview(self):
        self.ui_helper.click(self._OVERVIEW_LOCATOR, "Button overview")

    def open_market_watch(self):
        self.ui_helper.click(self._MARKET_WATCH_LOCATOR, "Button market watch")

    def open_exposure(self):
        self.ui_helper.click(self._EXPOSURE_LOCATOR, "Button exposure")

    def open_users(self):
        self.ui_helper.click(self._USERS_LOCATOR, "Button users")

    def click_logout(self):
        self.ui_helper.click(self._LOGOUT_LOCATOR, "Button logout")