import time

from selenium.webdriver.remote.webelement import WebElement
from base.base_page import BasePage

from pages.price_channel_page.components.rules.components.create import Create



class Rules(BasePage):


    _ROWS_LOCATOR = ".//table[@id='QuoteStreamConfigRules_content_table']//tr"
    _CELLS_LOCATOR = ".//td"
    _DELETE_BUTTON_LOCATOR = ".//td[@name='DeleteButton']"
    _ENABLE_DISABLE_CHECKBOX_LOCATOR = ".//td[@name='QuoteStreamConfigRulesisEnabled']"

    _CREATE_BUTTON_LOCATOR = "//button[@id='CreateRule']"
    _SAVE_RULES_BUTTON_LOCATOR = "//button[@id='SaveRules']"
    _CANCEL_BUTTON_LOCATOR = "//button[@id='QuoteStreamConfigRules_cancel']"
    _EXPORT_BUTTON_LOCATOR = "//div[@id='QuoteStreamConfigRules_toolbarItems']//button[@id='SaveToTsv']"
    _IMPORT_BUTTON_LOCATOR = "//div[@id='QuoteStreamConfigRules_toolbarItems']//button[@id='LoadFromTsv']"

    _BUTTON_SAVE_OK_LOCATOR = "//div[@id='quoteStreamRulesCloseConfirmDialog']//button[text()='OK']"
    _BUTTON_SAVE_CANCEL_LOCATOR = "//div[@id='quoteStreamRulesCloseConfirmDialog']//button[text()='Cancel']"

    _BUTTON_CLOSE_LOCATOR = "//div[@id='quoteStreamRulesDialog_dialog-header']//button[@type='button']"


    def __init__(self, driver):
        super().__init__(driver)
        self.create = Create(driver)





    @property
    def _rows(self) -> list[WebElement]:
        # table = self._table
        return self.ui_helper.find_all(self._ROWS_LOCATOR, wait=True)

    def get_row_content(self, number_of_row) -> list:
        row = self._rows[number_of_row - 1]
        return [cell.text for cell in row.find_elements(*self._CELLS_LOCATOR)]

    def find_row_by_username(self, username):
        for _ in range(3):  # три попытки
            for i, row in enumerate(self._rows, start=1):
                if username in self.get_row_content(i):
                    assert True  # нашли — тест проходит
                    return
            time.sleep(1)
        # если дошли до сюда — не нашли ни в одной из трёх попыток
        assert False, f"User '{username}' not found in any row after 3 attempts"


    def get_column_content(self, number_of_column) -> list:
        column_content = []
        for row in self._rows:
            cells = row.find_elements(*self._CELLS_LOCATOR)
            column_content.append(cells[number_of_column - 1].text)
        return column_content


    def click_delete_row_by_username(self, username):
        for row in self._rows:
            if username in self.get_row_content(self._rows.index(row) + 1):
                row.find_element(*self._DELETE_BUTTON_LOCATOR).click()
                break

    def click_enable_disable_by_username(self, username):
        for row in self._rows:
            if username in self.get_row_content(self._rows.index(row) + 1):
                row.find_element(*self._ENABLE_DISABLE_CHECKBOX_LOCATOR).click()
                break

    def open_create(self):
        self.ui_helper.click(self._CREATE_BUTTON_LOCATOR)

    def save_rules(self):
        self.ui_helper.click(self._SAVE_RULES_BUTTON_LOCATOR)
        self.ui_helper.click(self._BUTTON_SAVE_OK_LOCATOR)

    def click_cancel(self):
        self.ui_helper.click(self._CANCEL_BUTTON_LOCATOR)


    def click_export(self):
        self.ui_helper.click(self._EXPORT_BUTTON_LOCATOR)

    def click_import(self):
        self.ui_helper.click(self._IMPORT_BUTTON_LOCATOR)

    def click_close(self):
        self.ui_helper.click(self._BUTTON_CLOSE_LOCATOR)

