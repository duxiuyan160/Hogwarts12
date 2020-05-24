import pytest

from appium_xueqiu_po.page.search_page import SearchPage
from appium import webdriver


class TestSearch:
    def setup(self):
        self.search = SearchPage()

    @pytest.mark.parametrize("key,stocktype",[('ali','BABA'),('xiaomi','01810')])
    def test_search(self,key,stocktype):
        assert self.search.searchkey(key,stocktype) == "已添加"
