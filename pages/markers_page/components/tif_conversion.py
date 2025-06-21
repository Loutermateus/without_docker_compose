import time
from selenium.common import StaleElementReferenceException

from base.base_page import BasePage
from selenium.webdriver.remote.webelement import WebElement




class TifConversion(BasePage):


    _ROWS_LOCATOR = "//table[@id='TIFConversionRulesGrid_content_table']//tr"
    _CELLS_LOCATOR = ".//td"
    _EDIT_FOK_TO_GTC_CHECKBOX = ".//input[@name='fokToGTC']"
    _EDIT_IOC_TO_GTC_CHECKBOX = ".//input[@name='iocToGTC']"


    _SAVE_RULES_LOCATOR = "//button[@id='SaveRules']"
    _CANCEL_RULES_LOCATOR = "//button[@id='TIFConversionRulesGrid_cancel']"
    _FILTER_FIELD_LOCATOR = "//input[@id='filterBox']"

    _BUTTON_OK_LOCATOR = "//div[@id='TIFConversionRulesGridCloseConfirmDialog']//button[text()='OK']"
    _BUTTON_CANCEL_LOCATOR = "//div[@id='TIFConversionRulesGridCloseConfirmDialog']//button[text()='Cancel']"

    _BATCH_DROPDOWN_SELECT_LOCATOR = "//button[@id='selectAllSplitBtn']//span[@class='e-btn-icon e-icons e-icon-right e-caret']"
    _SELECT_ALL_LOCATOR = "//li[@id='SelectallItem']"
    _SELECT_ALL_FOK_TO_GTC_LOCATOR = "//li[@id='SelectallFOKtoGTCItem']"
    _SELECT_ALL_IOC_TO_GTC_LOCATOR = "//li[@id='SelectallIOCtoGTCItem']"


    _BATCH_DROPDOWN_DESELECT_LOCATOR = "//button[@id='deselectAllSplitBtn']//span[@class='e-btn-icon e-icons e-icon-right e-caret']"
    _DESELECT_ALL_LOCATOR = "//li[@id='DeselectallItem']"
    _DESELECT_ALL_FOK_TO_GTC_LOCATOR = "//li[@id='DeselectallFOKtoGTCItem']"
    _DESELECT_ALL_IOC_TO_GTC_LOCATOR = "//li[@id='DeselectallIOCtoGTCItem']"


    @property
    def _rows(self) -> list[WebElement]:
        # table = self._table
        return self.ui_helper.find_all(self._ROWS_LOCATOR, wait=True)

    @property
    def row_count(self) -> int:
        return len(self._rows)

    def get_row_content(self, number_of_row) -> list:
        row = self._rows[number_of_row - 1]
        return [cell.text for cell in row.find_elements(*self._CELLS_LOCATOR)]

    def click_select_fok_to_gtc_checkbox_by_username(self, username):
        for row in self._rows:
            if username in self.get_row_content(self._rows.index(row) + 1):
                cell = row.find_element(*self._EDIT_FOK_TO_GTC_CHECKBOX)
                if cell.is_selected():
                    continue
                else:
                    cell.click()
                break

    def click_deselect_fok_to_gtc_checkbox_by_username(self, username):
        for row in self._rows:
            if username in self.get_row_content(self._rows.index(row) + 1):
                cell = row.find_element(*self._EDIT_FOK_TO_GTC_CHECKBOX)
                if cell.is_selected():
                    cell.click()
                else:
                    continue
                break



    def click_select_ioc_to_gtc_checkbox_by_username(self, username):
        for row in self._rows:
            if username in self.get_row_content(self._rows.index(row) + 1):
                cell = row.find_element(*self._EDIT_IOC_TO_GTC_CHECKBOX)
                if cell.is_selected():
                    continue
                else:
                    cell.click()
                break



    def click_deselect_ioc_to_gtc_checkbox_by_username(self, username):
        for row in self._rows:
            if username in self.get_row_content(self._rows.index(row) + 1):
                cell = row.find_element(*self._EDIT_FOK_TO_GTC_CHECKBOX)
                if cell.is_selected():
                    cell.click()
                else:
                    continue
                break

    def check_select_fok_to_gtc_checkbox_by_username(self, username):
        for _ in range(3):
            try:
                for index, row in enumerate(self._rows, start=1):
                    if username in self.get_row_content(index):
                        cell = row.find_element(*self._EDIT_FOK_TO_GTC_CHECKBOX)
                        assert cell.is_selected(), f"Checkbox for '{username}' is not selected"
                        break
                else:
                    raise AssertionError(f"Row with username '{username}' not found")
            except StaleElementReferenceException:
                time.sleep(1)

    def check_select_ioc_to_gtc_checkbox_by_username(self, username):
        for index, row in enumerate(self._rows, start=1):
            if username in self.get_row_content(index):
                cell = row.find_element(*self._EDIT_IOC_TO_GTC_CHECKBOX)
                assert cell.is_selected(), f"Checkbox for '{username}' is not selected"
                break
        else:
            raise AssertionError(f"Row with username '{username}' not found")



    def click_save_rules(self):
        self.ui_helper.click(self._SAVE_RULES_LOCATOR)

    def click_ok(self):
        self.ui_helper.click(self._BUTTON_OK_LOCATOR)




    def click_cancel(self):
        self.ui_helper.click(self._CANCEL_RULES_LOCATOR)


    def select_all(self):
        self.ui_helper.click(self._BATCH_DROPDOWN_SELECT_LOCATOR)
        self.ui_helper.click(self._SELECT_ALL_LOCATOR)

    def select_all_fok_to_gtc(self):
        self.ui_helper.click(self._BATCH_DROPDOWN_SELECT_LOCATOR)
        self.ui_helper.click(self._SELECT_ALL_FOK_TO_GTC_LOCATOR)

    def select_all_ioc_to_gtc(self):
        self.ui_helper.click(self._BATCH_DROPDOWN_SELECT_LOCATOR)
        self.ui_helper.click(self._SELECT_ALL_IOC_TO_GTC_LOCATOR)


    def deselect_all(self):
        self.ui_helper.click(self._BATCH_DROPDOWN_DESELECT_LOCATOR)
        self.ui_helper.click(self._DESELECT_ALL_LOCATOR)

    def deselect_all_fok_to_gtc(self):
        self.ui_helper.click(self._BATCH_DROPDOWN_DESELECT_LOCATOR)
        self.ui_helper.click(self._DESELECT_ALL_FOK_TO_GTC_LOCATOR)

    def deselect_all_ioc_to_gtc(self):
        self.ui_helper.click(self._BATCH_DROPDOWN_DESELECT_LOCATOR)
        self.ui_helper.click(self._DESELECT_ALL_IOC_TO_GTC_LOCATOR)


    def fill_filter(self, text):
        self.ui_helper.find(self._FILTER_FIELD_LOCATOR, wait=True)
        self.ui_helper.fill(self._FILTER_FIELD_LOCATOR, text, clear=True)








