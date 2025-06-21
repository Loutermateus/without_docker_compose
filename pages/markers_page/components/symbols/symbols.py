from base.base_page import BasePage
from selenium.webdriver.remote.webelement import WebElement
import os





class Symbols(BasePage):

    _ROWS_LOCATOR = "//table[@id='ProviderModifier_content_table']//tr"
    _CELLS_LOCATOR = ".//td"
    _EDIT_BUTTON = "//td[@name='EditButton']"
    _DELETE_BUTTON = "//td[@name='DeleteButton']"


    _CREATE_BUTTON_LOCATOR = "//button[@id='CreateRule']"
    _EXPORT_BUTTON_LOCATOR = "//button[@id='SaveToTsv']"
    _IMPORT_BUTTON_LOCATOR = "//button[@id='LoadFromTsv']"

    _UPLOAD_FIELD_LOCATOR = "//input[@id='tsvFile']"
    _IMPORT_CLICK_LOCATOR = "//button[text()='Import']"


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



    def open_create(self):
        self.ui_helper.click(self._CREATE_BUTTON_LOCATOR)

    def data_export(self):
        self.ui_helper.click(self._EXPORT_BUTTON_LOCATOR)

    def data_import(self):
        self.ui_helper.click(self._IMPORT_BUTTON_LOCATOR)
        field_for_import = self.wait.until(self.EC.presence_of_element_located(self._UPLOAD_FIELD_LOCATOR))

        file_path = os.path.realpath(
            os.path.join(os.getcwd(), "uploads", "upload_file.fortex.tsv")
        )

        field_for_import.send_keys(file_path)
        self.ui_helper.click(self._IMPORT_CLICK_LOCATOR)





