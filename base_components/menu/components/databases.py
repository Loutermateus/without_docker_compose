from base.base_page import BasePage




class Databases(BasePage):



    _DATABASES_DROPDOWN_LOCATOR = "//li[@id='header_menuitem_databases']"
    _DATABASES_ACTIVE_ORDERS_LOCATOR = "//a[@id='header_menuitem_databases_activeorders']"
    _DATABASES_POSITION_LOCATOR = "//a[@id='header_menuitem_databases_activepositions']"
    _DATABASES_ORDERS_LOCATOR = "//a[@id='header_menuitem_databases_orders']"
    _DATABASES_DEALS_LOCATOR = "//a[@id='header_menuitem_databases_deals']"
    _DATABASES_POSITION_HISTORY_LOCATOR = "//a[@id='header_menuitem_databases_positionshistory']"
    _DATABASES_ACCOUNT_HISTORY_LOCATOR = "//a[@id='header_menuitem_databases_accounthistory']"
    _DATABASES_EQUITY_REPORTS_LOCATOR = "//a[@id='header_menuitem_databases_equityreports']"



    def open_databases_active_orders(self):
        self.ui_helper.click(self._DATABASES_DROPDOWN_LOCATOR)
        self.ui_helper.click(self._DATABASES_ACTIVE_ORDERS_LOCATOR)


    def open_databases_position(self):
        self.ui_helper.click(self._DATABASES_DROPDOWN_LOCATOR)
        self.ui_helper.click(self._DATABASES_POSITION_LOCATOR)

    def open_databases_orders(self):
        self.ui_helper.click(self._DATABASES_DROPDOWN_LOCATOR)
        self.ui_helper.click(self._DATABASES_ORDERS_LOCATOR)


    def open_databases_deals(self):
        self.ui_helper.click(self._DATABASES_DROPDOWN_LOCATOR)
        self.ui_helper.click(self._DATABASES_DEALS_LOCATOR)

    def open_databases_position_history(self):
        self.ui_helper.click(self._DATABASES_DROPDOWN_LOCATOR)
        self.ui_helper.click(self._DATABASES_POSITION_HISTORY_LOCATOR)

    def open_databases_account_history(self):
        self.ui_helper.click(self._DATABASES_DROPDOWN_LOCATOR)
        self.ui_helper.click(self._DATABASES_ACCOUNT_HISTORY_LOCATOR)

    def open_databases_equity_reports(self):
        self.ui_helper.click(self._DATABASES_DROPDOWN_LOCATOR)
        self.ui_helper.click(self._DATABASES_EQUITY_REPORTS_LOCATOR)