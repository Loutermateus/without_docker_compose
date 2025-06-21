from base.base_page import BasePage




class Delete(BasePage):



    _DELETE_BUTTON_LOCATOR = "//button[text()='Delete']"
    _CANCEL_BUTTON_LOCATOR = "//div[@id='dialog']//button[text()='Cancel']"



    def click_delete(self):
        self.ui_helper.click(self._DELETE_BUTTON_LOCATOR, "Button delete")

    def click_cancel(self):
        self.ui_helper.click(self._CANCEL_BUTTON_LOCATOR, "Button cancel")
