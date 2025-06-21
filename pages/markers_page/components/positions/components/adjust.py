from base.base_page import BasePage


class Adjust(BasePage):



    _DROPDOWN_LOCATOR = "//span[@aria-labelledby='Symbol_hidden']//span[@class='e-input-group-icon e-ddl-icon e-search-icon']"
    _SYMBOL_DROPDOWN_LOCATORS = "//li[@role='option']"

    _PRICE_FIELD_LOCATOR = "//input[@id='Price']"
    _VOLUME_FIELD_LOCATOR = "//input[@id='Volume']"
    _COMMENT_FIELD_LOCATOR = "//input[@id='Comment']"
    _SELL_BUTTON_LOCATOR = "//button[@id='button-submit-sell']"
    _BUY_BUTTON_LOCATOR = "//button[@id='button-submit-buy']"

    _OK_BUTTON_LOCATOR = "//button[text()='OK']"
    _CANCEL_BUTTON_LOCATOR = "//div[@id='confirmAdjustPositionsDialog']//button[text()='Cancel']"


    def fill_symbol(self, market_type):
        self.ui_helper.click(self._DROPDOWN_LOCATOR)
        elements = self.ui_helper.find_all(self._SYMBOL_DROPDOWN_LOCATORS, wait=True)
        for element in elements:
            if market_type in element.text:
                element.click()

    def fill_price(self, text):
        self.ui_helper.fill(self._PRICE_FIELD_LOCATOR, text)

    def fill_volume(self, text):
        self.ui_helper.fill(self._VOLUME_FIELD_LOCATOR, text)

    def fill_comments(self, text):
        self.ui_helper.fill(self._COMMENT_FIELD_LOCATOR, text)

    def click_buy(self):
        self.ui_helper.click(self._BUY_BUTTON_LOCATOR)

    def click_sell(self):
        self.ui_helper.click(self._SELL_BUTTON_LOCATOR)

    def click_ok(self):
        self.ui_helper.click(self._OK_BUTTON_LOCATOR)

    def click_cancel(self):
        self.ui_helper.click(self._CANCEL_BUTTON_LOCATOR)

