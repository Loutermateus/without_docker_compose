from base.base_page import BasePage
from selenium.webdriver.remote.webelement import WebElement

from pages.markers_page.components.positions.components.send_order import SendOrder
from pages.markers_page.components.positions.components.adjust import Adjust





class Positions(BasePage):


    _ROWS_LOCATOR = ".//table[@id='SyntheticPositions_content_table']//tr"
    _CELLS_LOCATOR = ".//td"


    _ADJUST_BUTTON_LOCATOR = "//button[@id='Adjust']"
    _SEND_ORDER_BUTTON_LOCATOR = "//button[@id='Order']"

    _NONE_LOCATOR = "//div[@id='providerPositionsStatsDialog_title']"


    def __init__(self, driver):
        super().__init__(driver)
        self.adjust = Adjust(driver)
        self.send_order = SendOrder(driver)



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

    def open_adjust(self):
        self.ui_helper.click(self._ADJUST_BUTTON_LOCATOR)


    def open_send_order(self):
        self.ui_helper.click(self._SEND_ORDER_BUTTON_LOCATOR)


    def click_to_none(self):
        self.wait.until(self.EC.visibility_of_element_located(self._NONE_LOCATOR))










