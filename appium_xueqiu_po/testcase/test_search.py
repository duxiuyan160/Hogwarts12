import pytest
from appium.webdriver.common.mobileby import MobileBy

from appium_xueqiu_po.page.app import App
from appium_xueqiu_po.page.search_page import SearchPage
from appium import webdriver


class TestSearch:
    def setup(self):
        self.search = App().start().main().goto_market().goto_search()

    #@pytest.mark.parametrize("key,stocktype",[('alibaba','BABA'),('xiaomi','01810')])
    def test_search(self):
        assert self.search.searchkey('alibaba','BABA') == "已添加"
