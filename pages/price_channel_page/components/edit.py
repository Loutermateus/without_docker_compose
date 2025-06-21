from base.base_page import BasePage




class Edit(BasePage):


    _NAME_FIELD_LOCATOR = "//input[@id='Name']"
    _ENABLED_CHECKBOX_LOCATOR = "//span[@class='e-icons e-frame e-check']"

    _TAKERS_DROPDOWN_LOCATOR = "//div[@class='e-multi-select-wrapper']"
    _SELECT_ALL_LOCATOR = "//span[@class='e-all-text']"

    _BUTTON_SAVE_LOCATOR = "//button[text()='Save']"


    def select_unselect_all_takers(self):
        self.ui_helper.click(self._TAKERS_DROPDOWN_LOCATOR)
        self.ui_helper.click(self._SELECT_ALL_LOCATOR)

    def click_enable_disable(self):
        self.ui_helper.click(self._ENABLED_CHECKBOX_LOCATOR)

    def fill_name(self, name):
        self.ui_helper.fill(self._NAME_FIELD_LOCATOR, name, clear=True)

    def click_save(self):
        self.ui_helper.click(self._BUTTON_SAVE_LOCATOR)


