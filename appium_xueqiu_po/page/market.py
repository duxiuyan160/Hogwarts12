from appium_xueqiu_po.page.base_page import BasePage
from appium_xueqiu_po.page.search_page import SearchPage


class Market(BasePage):
    def goto_search(self):
        return SearchPage(self._driver)