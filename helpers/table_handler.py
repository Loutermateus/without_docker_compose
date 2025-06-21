from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement



class TableHandler:

    TABLE_LOCATOR = "//div[@role='table']"
    ROWS_LOCATOR = ".//div[@class='oxd-table-body']//div[@role='row']"
    CELLS_LOCATOR =  ".//div[@role='cell']"
    DELETE_BUTTON = ".//div[@class='oxd-table-cell-actions']//button[.//i[contains(@class, 'bi-trash')]]"
    EDIT_BUTTON = ".//div[@class='oxd-table-cell-actions']//button[.//i[contains(@class, 'bi-pencil-fill')]]"

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @property
    def _table(self) -> WebElement:
        return self.driver.find_element(*self.TABLE_LOCATOR)

    @property
    def _rows(self) -> list[WebElement]:
        table = self._table
        return table.find_elements(*self.ROWS_LOCATOR)

    @property
    def row_count(self) -> int :
        return len(self._rows)

    def get_cell_content(self, number_of_row, number_of_column):
        row = self._rows[number_of_row - 1]
        cell = row.find_elements(*self.CELLS_LOCATOR)[number_of_column - 1]
        return cell.text



    def get_row_content(self, number_of_row) -> list :
        row = self._rows[number_of_row - 1]
        return [cell.text for cell in row.find_elements(*self.CELLS_LOCATOR)]


    def get_column_content(self,number_of_column) -> list :
        column_content = []
        for row in self._rows:
            cells = row.find_elements(*self.CELLS_LOCATOR)
            column_content.append(cells[number_of_column - 1].text)
        return column_content


    def select_row(self, number_of_row):
        row = self._rows[number_of_row - 1]
        if "Admin" in self.get_column_content(number_of_row)[2]:
            raise "NO, NO, its ADMIN"
        else:
            cell = row.find_elements(*self.CELLS_LOCATOR)[0]
            cell.click()

    def edit_row(self, number_of_row):
        row = self._rows[number_of_row - 1]
        row.find_element(*self.EDIT_BUTTON).click()


    def delete_row(self, number_of_row):
        row = self._rows[number_of_row - 1]
        if "Admin" in self.get_column_content(number_of_row)[2]:
            raise "NO, NO, its ADMIN"
        else:
            cell = row.find_element(*self.DELETE_BUTTON)
            cell.click()


    def edit_row_by_username(self, username):
        rows = self._rows
        for row in rows:
            if username in self.get_row_content(self._rows.index(row) + 1):
                row.find_element(*self.EDIT_BUTTON).click()
                break