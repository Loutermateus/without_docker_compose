from base.base_page import BasePage




class SendOrder(BasePage):


    _DROPDOWN_LOCATOR = "//span[@aria-labelledby='Symbol_hidden']//span[@class='e-input-group-icon e-ddl-icon e-search-icon']"
    _SYMBOL_DROPDOWN_LOCATORS = "//li[@role='option']"

    _PRICE_FIELD_LOCATOR = "//input[@id='Price']"
    _VOLUME_FIELD_LOCATOR = "//input[@id='Volume']"

    _TIF_DROPDOWN_LOCATOR = "//span[@aria-labelledby='TimeInForce_hidden']//span[@class='e-input-group-icon e-ddl-icon e-search-icon']"
    _IOC_LOCATOR = "//li[text()='IOC']"
    _FOK_LOCATOR = "//li[text()='FOK']"

    _COMMENT_FIELD_LOCATOR = "//input[@id='Comment']"
    _MARKET_BUTTON_LOCATOR = "//label[text()='Market']"

    def choose_tif_ioc(self):
        self.ui_helper.click(self._TIF_DROPDOWN_LOCATOR)
        self.ui_helper.click(self._IOC_LOCATOR)

    def choose_tif_fok(self):
        self.ui_helper.click(self._TIF_DROPDOWN_LOCATOR)
        self.ui_helper.click(self._FOK_LOCATOR)

    def click_market_button(self):
        self.ui_helper.click(self._MARKET_BUTTON_LOCATOR)

    def click_limit_button(self):
        self.ui_helper.click(self._LIMIT_BUTTON_LOCATOR)


    def fill_symbol(self, market_type):
        self.ui_helper.click(self._DROPDOWN_LOCATOR)
        elements = self.ui_helper.find_all(self._SYMBOL_DROPDOWN_LOCATORS, wait=True)
        for element in elements:
            if market_type in element.text:
                element.click()

    def fill_price(self):
        self.ui_helper.fill(self._PRICE_FIELD_LOCATOR)


    def fill_volume(self):
        self.ui_helper.fill(self._VOLUME_FIELD_LOCATOR)