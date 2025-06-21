from base.base_page import BasePage
from config.urls import Urls
from selenium.webdriver.remote.webelement import WebElement


from pages.takers_page.components.create import Create
from pages.takers_page.components.edit import Edit
from pages.takers_page.components.delete import Delete



class TakerPage(BasePage):


    _PAGE_URL = Urls.TAKERS_PAGE

    _ROWS_LOCATOR = ".//table[@id ='ConsumersV3_content_table']//tr"
    _CELLS_LOCATOR = ".//td"
    _DELETE_BUTTON_LOCATOR = ".//td[@name='DeleteButton']"
    _EDIT_BUTTON_LOCATOR = ".//td[@name='EditButton']"
    _POSITION_BUTTON_LOCATOR = ".//td[@name='PositionsButton']"
    _SYMBOLS_MAPPING_BUTTON_LOCATOR = ".//td[@name='MappingButton']"

    _CHOOSE_COLUMNS_BUTTON_LOCATOR = "//button[@id='ChooseColumns']"
    _CREATE_BUTTON_LOCATOR = "//button[@id='Create']"
    _FILTER_FIELD_LOCATOR = "//input[@id='filterBox']"


    def __init__(self, driver):
        super().__init__(driver)
        self.create = Create(driver)
        self.edit = Edit(driver)
        self.delete = Delete(driver)



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
            if username in  self.get_row_content(self._rows.index(row) + 1):
                row.find_element(*self._DELETE_BUTTON_LOCATOR).click()
                break

    def click_positions_by_username(self, username):
        for row in self._rows:
            if username in  self.get_row_content(self._rows.index(row) + 1):
                row.find_element(*self._POSITION_BUTTON_LOCATOR).click()
                break

    def click_symbols_mapping_by_username(self, username):
        for row in self._rows:
            if username in  self.get_row_content(self._rows.index(row) + 1):
                row.find_element(*self._SYMBOLS_MAPPING_BUTTON_LOCATOR).click()
                break

    def cant_find_row_by_username(self, username):
        for i, row in enumerate(self._rows, start=1):
            if username not in self.get_row_content(i):
                assert True  # нашли — тест проходит
            else:
                assert False, "Have this row"

    def choose_columns(self):
        self.ui_helper.click(self._CHOOSE_COLUMNS_BUTTON_LOCATOR)


    def open_create(self):
        self.ui_helper.click(self._CREATE_BUTTON_LOCATOR)