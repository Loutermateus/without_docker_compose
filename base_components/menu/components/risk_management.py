from base.base_page import BasePage




class RiskManagement(BasePage):


    _RISK_MANAGEMENT_DROPDOWN_LOCATOR = "//li[@id='header_menuitem_riskmanagement']"
    _RISK_MANAGEMENT_META_TRADER_SERVER_LOCATOR = "//a[@id='header_menuitem_riskmanagement_servers']"
    _RISK_MANAGEMENT_SUMMARY_LOCATOR = "//a[@id='header_menuitem_riskmanagement_dailydata']"
    _RISK_MANAGEMENT_BALANCES_EQUITIES_LOCATOR = "//a[@id='header_menuitem_riskmanagement_balancesequities']"
    _RISK_MANAGEMENT_WINNERS_LOSERS_LOCATOR = "//a[@id='header_menuitem_riskmanagement_winnerslosers']"
    _RISK_MANAGEMENT_ACCOUNTS_VOLUMES_LOCATOR = "//a[@id='header_menuitem_riskmanagement_accountsvolumes']"




    def open_risk_management_meta_trader_server(self):
        self.ui_helper.click(self._RISK_MANAGEMENT_DROPDOWN_LOCATOR)
        self.ui_helper.click(self._RISK_MANAGEMENT_META_TRADER_SERVER_LOCATOR)

    def open_risk_management_summary(self):
        self.ui_helper.click(self._RISK_MANAGEMENT_DROPDOWN_LOCATOR)
        self.ui_helper.click(self._RISK_MANAGEMENT_SUMMARY_LOCATOR)

    def open_risk_management_balances_equities(self):
        self.ui_helper.click(self._RISK_MANAGEMENT_DROPDOWN_LOCATOR)
        self.ui_helper.click(self._RISK_MANAGEMENT_BALANCES_EQUITIES_LOCATOR)

    def open_risk_management_winners_losers(self):
        self.ui_helper.click(self._RISK_MANAGEMENT_DROPDOWN_LOCATOR)
        self.ui_helper.click(self._RISK_MANAGEMENT_WINNERS_LOSERS_LOCATOR)

    def open_risk_management_meta_account_volumes(self):
        self.ui_helper.click(self._RISK_MANAGEMENT_DROPDOWN_LOCATOR)
        self.ui_helper.click(self._RISK_MANAGEMENT_ACCOUNTS_VOLUMES_LOCATOR)