from base.base_page import BasePage




class Settings(BasePage):



    _SETTINGS_DROPDOWN_LOCATOR = "//li[@id='header_menuitem_settings']"
    _SETTINGS_SYMBOLS_LOCATOR = "//a[@id='header_menuitem_settings_symbols']"
    _SETTINGS_MARKET_LOCATOR = "//a[@id='header_menuitem_settings_makers']"
    _SETTINGS_TAKERS_LOCATOR = "//a[@id='header_menuitem_settings_takers']"
    _SETTINGS_PRICE_CHANNEL_LOCATOR = "//a[@id='header_menuitem_settings_pricechannels']"
    _SETTINGS_ACCOUNTS_LOCATOR = "//a[@id='header_menuitem_settings_marginaccounts']"
    _SETTINGS_B_BOOK_ACCOUNTS_LOCATOR = "//a[@id='header_menuitem_settings_bbookaccounts']"
    _SETTINGS_RISK_PROFILES_LOCATOR = "//a[@id='header_menuitem_settings_riskprofiles']"
    _SETTINGS_EVENTS_LOCATOR = "//a[@id='header_menuitem_settings_scheduledevents']"
    _SETTINGS_LIMITS_PROFILES_LOCATOR = "//a[@id='header_menuitem_settings_accountlimitsprofiles']"


    def open_setting_symbols(self):
        self.ui_helper.click(self._SETTINGS_DROPDOWN_LOCATOR)
        self.ui_helper.click(self._SETTINGS_SYMBOLS_LOCATOR)

    def open_setting_market(self):
        self.ui_helper.click(self._SETTINGS_DROPDOWN_LOCATOR)
        self.ui_helper.click(self._SETTINGS_MARKET_LOCATOR)


    def open_setting_takers(self):
        self.ui_helper.click(self._SETTINGS_DROPDOWN_LOCATOR)
        self.ui_helper.click(self._SETTINGS_TAKERS_LOCATOR)

    def open_setting_price_channel(self):
        self.ui_helper.click(self._SETTINGS_DROPDOWN_LOCATOR)
        self.ui_helper.click(self._SETTINGS_PRICE_CHANNEL_LOCATOR)

    def open_setting_accounts(self):
        self.ui_helper.click(self._SETTINGS_DROPDOWN_LOCATOR)
        self.ui_helper.click(self._SETTINGS_ACCOUNTS_LOCATOR)

    def open_setting_bbook_accounts(self):
        self.ui_helper.click(self._SETTINGS_DROPDOWN_LOCATOR)
        self.ui_helper.click(self._SETTINGS_B_BOOK_ACCOUNTS_LOCATOR)


    def open_setting_risk_profile(self):
        self.ui_helper.click(self._SETTINGS_DROPDOWN_LOCATOR)
        self.ui_helper.click(self._SETTINGS_RISK_PROFILES_LOCATOR)

    def open_setting_events(self):
        self.ui_helper.click(self._SETTINGS_DROPDOWN_LOCATOR)
        self.ui_helper.click(self._SETTINGS_EVENTS_LOCATOR)

    def open_setting_limits_profiles(self):
        self.ui_helper.click(self._SETTINGS_DROPDOWN_LOCATOR)
        self.ui_helper.click(self._SETTINGS_LIMITS_PROFILES_LOCATOR)



