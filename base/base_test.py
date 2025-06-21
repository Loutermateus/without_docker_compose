from pages.login_page.page import LoginPage
from base_components.menu.menu import Menu
from pages.markers_page.page import MarkersPage
from pages.users_page.page import UsersPage
from pages.takers_page.page import TakerPage
from pages.price_channel_page.page import PriceChannelPage

class BaseTest:

    def setup_method(self):
        self.login_page = lambda driver=self.driver: LoginPage(driver)
        self.menu = lambda driver=self.driver: Menu(driver)
        self.markers_pages = lambda driver=self.driver: MarkersPage(driver)
        self.users_page = lambda driver=self.driver: UsersPage(driver)
        self.taker_page = lambda driver=self.driver: TakerPage(driver)
        self.price_channel_page = lambda driver=self.driver: PriceChannelPage(driver)
