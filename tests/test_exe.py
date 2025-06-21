import allure

from base.base_test import BaseTest
import pytest

class TestExe(BaseTest):

    @allure.title("Test Login")
    def test_login(self):
        self.login_page().open()
        self.login_page().login()

    @allure.title("Test for change name")
    def test_create_marker_and_change_name_marker(self):
        self.login_page().open()
        self.login_page().login()
        self.menu().settings.open_setting_market()
        self.markers_pages().open_create()
        self.markers_pages().create.choose_enable()
        self.markers_pages().create.fill_name("berlin")
        self.markers_pages().create.fill_configuration("babu")
        self.markers_pages().create.fill_market_type("Fortex")
        self.markers_pages().create.choose_save_to_csv_file()
        self.markers_pages().create.choose_save_to_log_file()
        self.markers_pages().create.click_create()
        self.markers_pages().refresh_page()
        self.markers_pages().find_row_by_username("berlin")
        self.markers_pages().click_edit_row_by_username("berlin")
        self.markers_pages().edit.fill_market_type("OneZero")
        self.markers_pages().edit.fill_name("mike")
        self.markers_pages().edit.click_save()
        self.markers_pages().refresh_page()
        self.markers_pages().find_row_by_username("mike")
        self.markers_pages().click_delete_row_by_username("mike")
        self.markers_pages().delete.click_delete()
        self.markers_pages().refresh_page()




    @allure.title("Test adjust")
    def test_open_and_adjust_position(self):
        self.login_page().open()
        self.login_page().login()
        self.menu().settings.open_setting_market()
        self.markers_pages().open_create()
        self.markers_pages().create.choose_enable()
        self.markers_pages().create.fill_name("pogoda")
        self.markers_pages().create.fill_configuration("babu")
        self.markers_pages().create.fill_market_type("Fortex")
        self.markers_pages().create.choose_save_to_csv_file()
        self.markers_pages().create.choose_save_to_log_file()
        self.markers_pages().create.click_create()
        self.markers_pages().refresh_page()
        self.markers_pages().find_row_by_username("pogoda")
        self.markers_pages().open_action_position_by_name("pogoda")
        self.markers_pages().positions.open_adjust()
        self.markers_pages().positions.adjust.fill_symbol("EUR/USD$")
        self.markers_pages().positions.adjust.fill_price("200")
        self.markers_pages().positions.adjust.fill_volume("100")
        self.markers_pages().positions.adjust.fill_comments("basta")
        self.markers_pages().positions.adjust.click_buy()
        self.markers_pages().positions.adjust.click_ok()
        self.markers_pages().refresh_page()
        self.markers_pages().open_action_position_by_name("pogoda")
        self.markers_pages().positions.find_row_by_username("EUR/USD$")
        self.markers_pages().positions.open_adjust()
        self.markers_pages().positions.adjust.fill_symbol("EUR/USD$")
        self.markers_pages().positions.adjust.fill_price("200")
        self.markers_pages().positions.adjust.fill_volume("100")
        self.markers_pages().positions.adjust.fill_comments("basta")
        self.markers_pages().positions.adjust.click_sell()
        self.markers_pages().positions.adjust.click_ok()
        self.markers_pages().refresh_page()
        self.markers_pages().open_action_position_by_name("pogoda")
        self.markers_pages().positions.cant_find_row_by_username("EUR/USD$")
        self.markers_pages().refresh_page()
        self.markers_pages().click_delete_row_by_username("pogoda")
        self.markers_pages().delete.click_delete()
        self.markers_pages().refresh_page()


    @allure.title("Test TIF conversion")
    def test_set_tif_conversion(self):
        self.login_page().open()
        self.login_page().login()
        self.menu().settings.open_setting_market()
        self.markers_pages().open_create()
        self.markers_pages().create.choose_enable()
        self.markers_pages().create.fill_name("karavan")
        self.markers_pages().create.fill_configuration("babu")
        self.markers_pages().create.fill_market_type("OneZero")
        self.markers_pages().create.choose_save_to_csv_file()
        self.markers_pages().create.choose_save_to_log_file()
        self.markers_pages().create.click_create()
        self.markers_pages().refresh_page()
        self.markers_pages().find_row_by_username("karavan")
        self.markers_pages().open_action_tif_conversion_by_name("karavan")
        self.markers_pages().tif_conversion.click_select_fok_to_gtc_checkbox_by_username("denver")
        self.markers_pages().tif_conversion.click_select_fok_to_gtc_checkbox_by_username("fortex")
        self.markers_pages().tif_conversion.click_select_ioc_to_gtc_checkbox_by_username("hello")
        self.markers_pages().tif_conversion.click_save_rules()
        self.markers_pages().tif_conversion.click_ok()
        self.markers_pages().tif_conversion.check_select_fok_to_gtc_checkbox_by_username("denver")
        self.markers_pages().tif_conversion.check_select_fok_to_gtc_checkbox_by_username("fortex")
        self.markers_pages().tif_conversion.check_select_ioc_to_gtc_checkbox_by_username("hello")
        self.markers_pages().tif_conversion.deselect_all()
        self.markers_pages().tif_conversion.click_save_rules()
        self.markers_pages().tif_conversion.click_ok()
        self.markers_pages().refresh_page()
        self.markers_pages().click_delete_row_by_username("karavan")
        self.markers_pages().delete.click_delete()
        self.markers_pages().refresh_page()





    @pytest.mark.parametrize("add_users", [1], indirect=True)
    @allure.title("Test Param")
    def test_create_manager(self, add_users):
        manager = add_users[0]
        self.login_page().open()
        self.login_page().login_as("admin")
        self.menu().open_users()
        self.users_page().open_create()
        self.users_page().create.fill_market_type("Manager")
        self.users_page().create.fill_login()
        self.users_page().create.fill_password()
        self.users_page().create.click_create()
        self.users_page().refresh_page()
        self.users_page().find_row_by_username("LOGIN")

        #for manager
        self.login_page(manager).open()
        self.login_page(manager).login_as("manager")
        self.menu(manager).settings.open_setting_market()
        self.menu(manager).open_market_watch()
        self.menu(manager).click_logout()


        #for admin
        self.users_page().click_delete_row_by_username("LOGIN")
        self.users_page().delete.click_delete()
        self.users_page().refresh_page()
        self.users_page().cant_find_row_by_username("LOGIN")



    @allure.title("Test for user")
    def test_adjust_position_for_taker(self):
        self.login_page().open()
        self.login_page().login()
        self.menu().settings.open_setting_takers()
        self.taker_page().open_create()
        self.taker_page().create.fill_market_type("Takeprofit")
        self.taker_page().create.fill_taker("denver")
        self.taker_page().create.fill_account("alpaca")
        self.taker_page().create.fill_name("pablo")
        self.taker_page().create.choose_save_to_log_file()
        self.taker_page().create.choose_save_to_csv_file()
        self.taker_page().create.choose_enable()
        self.taker_page().create.click_create()
        self.taker_page().refresh_page()
        self.taker_page().find_row_by_username("pablo")
        self.menu().settings.open_setting_price_channel()
        self.price_channel_page().open_create()
        self.price_channel_page().create.select_unselect_all_takers()
        self.price_channel_page().create.fill_name("naso")
        self.price_channel_page().create.click_create()
        self.price_channel_page().refresh_page()
        self.price_channel_page().find_row_by_username("naso")
        self.price_channel_page().click_rules_row_by_username("naso")
        self.price_channel_page().rules.open_create()
        self.price_channel_page().rules.create.fill_hub_symbol("EUR/USD$")
        self.price_channel_page().rules.create.fill_taker_symbols("USD")
        self.price_channel_page().rules.create.click_create_rule()
        self.price_channel_page().rules.find_row_by_username("USD")
        self.price_channel_page().rules.save_rules()
        self.price_channel_page().rules.click_close()
        self.price_channel_page().refresh_page()
        self.price_channel_page().click_edit_row_by_username("naso")
        self.price_channel_page().edit.select_unselect_all_takers()
        self.price_channel_page().edit.click_save()
        self.price_channel_page().refresh_page()
        self.price_channel_page().click_delete_row_by_username("naso")
        self.price_channel_page().delete.click_delete()
        self.price_channel_page().refresh_page()
        self.price_channel_page().cant_find_row_by_username("naso")
        self.menu().settings.open_setting_takers()
        self.taker_page().click_edit_row_by_username("pablo")
        self.taker_page().edit.clear_all_accounts()
        self.taker_page().edit.click_save()
        self.taker_page().refresh_page()
        self.taker_page().click_delete_row_by_username("pablo")
        self.taker_page().delete.click_delete()
        self.taker_page().refresh_page()
        self.taker_page().cant_find_row_by_username("pablo")













