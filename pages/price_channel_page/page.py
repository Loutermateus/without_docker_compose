from selenium.webdriver.remote.webelement import WebElement
from base.base_page import BasePage
from config.urls import Urls

from pages.price_channel_page.components.create import Create
from pages.price_channel_page.components.edit import Edit
from pages.price_channel_page.components.delete import Delete
from pages.price_channel_page.components.rules.rules import Rules




class PriceChannelPage(BasePage):


    _PAGE_URL = Urls.CHANNEL_PRICE_PAGE

    _ROWS_LOCATOR = ".//table[@id ='QuoteStreams_content_table']//tr"
    _CELLS_LOCATOR = ".//td"
    _DELETE_BUTTON_LOCATOR = ".//td[@name='DeleteButton']"
    _EDIT_BUTTON_LOCATOR = ".//td[@name='EditButton']"
    _RULES_BUTTON_LOCATOR = ".//td[@name='RulesButton']"

    _CREATE_BUTTON_LOCATOR = "//button[@id='Create']"
    _FILTER_BUTTON_LOCATOR = "//button[@id='Filters']"
    _CLEAR_FILTER_BUTTON_LOCATOR = "//button[@id='ClearFilters']"
    _EXPORT_BUTTON_LOCATOR = "//button[@id='SaveToTsv']"


    def __init__(self, driver):
        super().__init__(driver)
        self.create = Create(driver)
        self.edit = Edit(driver)
        self.delete = Delete(driver)
        self.rules = Rules(driver)

    @property
    def _rows(self) -> list[WebElement]:
        # table = self._table
        return self.ui_helper.find_all(self._ROWS_LOCATOR, wait=True)

    def get_row_content(self, number_of_row) -> list:
        row = self._rows[number_of_row - 1]
        return [cell.text for cell in row.find_elements(*self._CELLS_LOCATOR)]

    def find_row_by_username(self, username):
        for i, row in enumerate(self._rows, start=1):
            if username in self.get_row_content(i):
                assert True  # нашли — тест проходит
                return
        assert False, "Dont have this row"  # не нашли — тест падает


    def cant_find_row_by_username(self, username):
        for i, row in enumerate(self._rows, start=1):
            if username not in self.get_row_content(i):
                assert True  # нашли — тест проходит
            else:
                assert False, "Have this row"

    def get_column_content(self, number_of_column) -> list:
        column_content = []
        for row in self._rows:
            cells = row.find_elements(*self._CELLS_LOCATOR)
            column_content.append(cells[number_of_column - 1].text)
        return column_content

    def edit_row(self, number_of_row):
        row = self._rows[number_of_row - 1]
        row.find_element(*self._EDIT_BUTTON_LOCATOR).click()

    def click_edit_row_by_username(self, username):
        for row in self._rows:
            if username in self.get_row_content(self._rows.index(row) + 1):
                row.find_element(*self._EDIT_BUTTON_LOCATOR).click()
                break

    def click_delete_row_by_username(self, username):
        for row in self._rows:
            if username in self.get_row_content(self._rows.index(row) + 1):
                row.find_element(*self._DELETE_BUTTON_LOCATOR).click()
                break

    def click_rules_row_by_username(self, username):
        for row in self._rows:
            if username in self.get_row_content(self._rows.index(row) + 1):
                row.find_element(*self._RULES_BUTTON_LOCATOR).click()
                break


    def open_create(self):
        self.ui_helper.click(self._CREATE_BUTTON_LOCATOR)

    def open_filter(self):
        self.ui_helper.click(self._FILTER_BUTTON_LOCATOR)

    def click_clear_filter(self):
        self.ui_helper.click(self._CLEAR_FILTER_BUTTON_LOCATOR)

    def click_export(self):
        self.ui_helper.click(self._EXPORT_BUTTON_LOCATOR)