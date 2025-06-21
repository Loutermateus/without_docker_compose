import time

from selenium.common import StaleElementReferenceException

from base.base_page import BasePage



class Create(BasePage):



    _CLICK_HUB_SYMBOL_DROPDOWN_LOCATOR = "//span[@aria-labelledby='CoreSymbolId_hidden']//span[@class='e-input-group-icon e-ddl-icon e-search-icon']"
    _HUB_SYMBOLS_LOCATORS = "//li[@role='option']"


    _TAKER_SYMBOLS_FIELD_LOCATOR = "//input[@id='OutputSymbolName']"
    _BUTTON_CREATE_LOCATOR ="//div[@id='createDialog-QuoteStreamConfigRules']//button[text()='Create']"




    def fill_taker_symbols(self, text):
        self.ui_helper.fill(self._TAKER_SYMBOLS_FIELD_LOCATOR, text, clear=True)

    def click_create_rule(self):
        for _ in range(1):
            try:
                self.ui_helper.click(self._BUTTON_CREATE_LOCATOR)
            except StaleElementReferenceException:
                time.sleep(1)

    def fill_hub_symbol(self, hub_symbol):
        for _ in range(1):
            try:
                self.ui_helper.click(self._CLICK_HUB_SYMBOL_DROPDOWN_LOCATOR)
                self.ui_helper.screenshot()
                elements = self.ui_helper.find_all(self._HUB_SYMBOLS_LOCATORS, wait=True)
                for element in elements:
                    if hub_symbol in element.text:
                        element.click()
            except StaleElementReferenceException:
                time.sleep(1)