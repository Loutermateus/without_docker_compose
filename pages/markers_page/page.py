from base.base_page import BasePage
from config.urls import Urls
from selenium.webdriver.remote.webelement import WebElement

from pages.markers_page.components.create import Create
from pages.markers_page.components.edit import Edit
from pages.markers_page.components.delete import Delete
from pages.markers_page.components.positions.positions import Positions
from pages.markers_page.components.tif_conversion import TifConversion
from pages.markers_page.components.symbols.symbols import Symbols

import allure


class MarkersPage(BasePage):

    _PAGE_URL = Urls.HOME_PAGE

    _ROWS_LOCATOR = ".//table[@id='Provider_content_table']//tr"
    _CELLS_LOCATOR = ".//td"
    _DELETE_BUTTON = ".//td[@name='DeleteButton']"
    _EDIT_BUTTON = ".//td[@name='EditButton']"
    _CREATE_BUTTON_LOCATOR = "//button[@id='Create']"

    _ACTION_LOCATOR = ".//div[@aria-label='Actions']"
    _REJECTION_STARS_LOCATOR = "//li[@aria-label='Rejection stats']"
    _POSITION_LOCATOR = "//li[@aria-label='Positions']"
    _SYMBOLS_LOCATOR = "//li[@aria-label='Symbols']"
    _CONVERSION_LOCATOR = "//li[@aria-label='TIF conversion']"
    _FIX_ROUTING_LOCATOR = "//li[@aria-label='FIX routing']"





    def __init__(self, driver):
        super().__init__(driver)
        self.create = Create(driver)
        self.edit = Edit(driver)
        self.delete = Delete(driver)
        self.positions = Positions(driver)
        self.tif_conversion = TifConversion(driver)
        self.symbols = Symbols(driver)




    @property
    def _rows(self) -> list[WebElement]:
        # table = self._table
        return self.ui_helper.find_all(self._ROWS_LOCATOR, wait=True)

    @property
    def row_count(self) -> int:
        return len(self._rows)



    def get_cell_content(self, number_of_row, number_of_column):
        row = self._rows[number_of_row - 1]
        cell = row.find_elements(*self._CELLS_LOCATOR)[number_of_column - 1]
        return cell.text

    def get_row_content(self, number_of_row) -> list:
        row = self._rows[number_of_row - 1]
        return [cell.text for cell in row.find_elements(*self._CELLS_LOCATOR)]

    def find_row_by_username(self, username):
        for i, row in enumerate(self._rows, start=1):
            if username in self.get_row_content(i):
                assert True  # нашли — тест проходит
                self.ui_helper.screenshot()
                return
        assert False, "Dont have this row"  # не нашли — тест падает


    def get_column_content(self, number_of_column) -> list:
        column_content = []
        for row in self._rows:
            cells = row.find_elements(*self._CELLS_LOCATOR)
            column_content.append(cells[number_of_column - 1].text)
        return column_content

    def select_row(self, number_of_row):
        row = self._rows[number_of_row - 1]
        if "Admin" in self.get_column_content(number_of_row)[2]:
            raise Exception("NO, NO, it's ADMIN")
        else:
            cell = row.find_elements(*self._CELLS_LOCATOR)[0]
            cell.click()

    def edit_row(self, number_of_row):
        row = self._rows[number_of_row - 1]
        row.find_element(*self._EDIT_BUTTON).click()

    def delete_row(self, number_of_row):
        row = self._rows[number_of_row - 1]
        if "Admin" in self.get_column_content(number_of_row)[2]:
            raise Exception("NO, NO, it's ADMIN")
        else:
            cell = row.find_element(*self._DELETE_BUTTON)
            cell.click()

    def click_edit_row_by_username(self, username):
        for row in self._rows:
            if username in self.get_row_content(self._rows.index(row) + 1):
                row.find_element(*self._EDIT_BUTTON).click()
                break

    def click_delete_row_by_username(self, username):
        for row in self._rows:
            if username in  self.get_row_content(self._rows.index(row) + 1):
                row.find_element(*self._DELETE_BUTTON).click()
                break

    def open_action_rejection_star_by_name(self, name):
        for row in self._rows:
            if name in self.get_row_content(self._rows.index(row) + 1):
                row.find_element(*self._ACTION_LOCATOR).click()
                self.ui_helper.click(self._REJECTION_STARS_LOCATOR)
                break

    @allure.step("Step")
    def open_action_position_by_name(self, name):
        for row in self._rows:
            if name in self.get_row_content(self._rows.index(row) + 1):
                row.find_element(*self._ACTION_LOCATOR).click()
                self.ui_helper.click(self._POSITION_LOCATOR)
                break

    def open_action_symbols_by_name(self, name):
        for row in self._rows:
            if name in self.get_row_content(self._rows.index(row) + 1):
                row.find_element(*self._ACTION_LOCATOR).click()
                self.ui_helper.click(self._SYMBOLS_LOCATOR)
                break

    def open_action_tif_conversion_by_name(self, name):
        for row in self._rows:
            if name in self.get_row_content(self._rows.index(row) + 1):
                row.find_element(*self._ACTION_LOCATOR).click()
                self.ui_helper.click(self._CONVERSION_LOCATOR)
                break

    def open_action_fix_routing_by_name(self, name):
        for row in self._rows:
            if name in self.get_row_content(self._rows.index(row) + 1):
                row.find_element(*self._ACTION_LOCATOR).click()
                time.sleep(3)
                self.ui_helper.click(self._FIX_ROUTING_LOCATOR)
                break

    def open_create(self):
        self.ui_helper.click(self._CREATE_BUTTON_LOCATOR)




