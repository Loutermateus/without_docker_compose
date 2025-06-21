from base.base_page import BasePage



class Edit(BasePage):


    _NAME_FIELD_LOCATOR = "//input[@id='Name']"
    _TEXT_AREA_LOCATOR = "//textarea[@id='ConnectionString']"
    _SAVE_QUOTES_TO_LOG_FILE_LOCATOR = "//label[@for='IsQuoteLoggingEnabled']//span[@class='e-icons e-frame']"
    _SAVE_QUOTES_TO_CSV_FILE_LOCATOR = "//label[@for='SaveQuotesToCsvLog']//span[@class='e-icons e-frame']"
    _CHECKBOX_ENABLE_LOCATOR = "//label[@for='IsEnabled']//span[@class='e-icons e-frame']"
    _SAVE_BUTTON_LOCATOR = "//div[@id='editDialog-ConsumersV3']//button[text()='Save']"
    _CLOSE_BUTTON_LOCATOR = "//div[@id='createDialog-Provider_dialog-header']//button[@type='button']"

    _BUTTON_FILL_CONFIGURATION_LOCATOR = "//button[@id='button-fill']"
    _BUTTON_YES_LOCATOR = "//button[text()='Yes']"
    _BUTTON_NO_LOCATOR = "//button[text()='No']"


    _MARKER_TYPE_LOCATORS = "//li[@role='option']"
    _CLICK_MARKER_DROPDOWN_LOCATOR = "//span[@aria-labelledby='ConsumerTypeId_hidden']//span[@class='e-input-group-icon e-ddl-icon e-search-icon']"

    _CLICK_ACCOUNT_DROPDOWN_LOCATOR = "//span[@aria-labelledby='MarginAccountId_hidden']//span[@class='e-input-group-icon e-ddl-icon e-search-icon']"
    _CLEAR_ALL_BUTTON_LOCATOR = "//span[@aria-labelledby='MarginAccountId_hidden']//span[@class='e-clear-icon e-clear-icon-hide']"
    _ACCOUNT_TYPE_LOCATORS = "//li[@role='option']"

    _CLICK_DROPCOPY_DROPDOWN_LOCATOR = "//span[@aria-labelledby='DropcopyToConsumerId_hidden']//span[@class='e-input-group-icon e-ddl-icon e-search-icon']"
    _DROPCOP_TYPE_LOCATORS = "//li[@role='option']"






    def fill_name(self, name):
        self.ui_helper.fill(self._NAME_FIELD_LOCATOR, name, clear=True)

    def fill_configuration(self, text):
        self.ui_helper.fill(self._TEXT_AREA_LOCATOR, text, clear=True)

    def choose_save_to_log_file(self):
        self.ui_helper.click(self._SAVE_QUOTES_TO_LOG_FILE_LOCATOR)

    def choose_save_to_csv_file(self):
        self.ui_helper.click(self._SAVE_QUOTES_TO_CSV_FILE_LOCATOR)

    def fill_market_type(self, market_type):
        self.ui_helper.click(self._CLICK_MARKER_DROPDOWN_LOCATOR)
        elements = self.ui_helper.find_all(self._MARKER_TYPE_LOCATORS, wait=True)
        for element in elements:
            if market_type in element.text:
                element.click()

    def fill_account(self, account):
        self.ui_helper.click(self._CLICK_ACCOUNT_DROPDOWN_LOCATOR)
        elements = self.ui_helper.find_all(self._MARKER_TYPE_LOCATORS, wait=True)
        for element in elements:
            if account in element.text:
                element.click()

    def clear_all_accounts(self):
        self.ui_helper.click(self._CLEAR_ALL_BUTTON_LOCATOR)

    def fill_taker(self, taker):
        self.ui_helper.click(self._CLICK_DROPCOPY_DROPDOWN_LOCATOR)
        elements = self.ui_helper.find_all(self._MARKER_TYPE_LOCATORS, wait=True)
        for element in elements:
            if taker in element.text:
                element.click()

    def choose_enable(self):
        self.ui_helper.click(self._CHECKBOX_ENABLE_LOCATOR)

    def click_save(self):
        self.ui_helper.click(self._SAVE_BUTTON_LOCATOR)

    def click_close(self):
        self.ui_helper.click(self._CLOSE_BUTTON_LOCATOR)


