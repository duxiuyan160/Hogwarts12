from huzhugou_po.page.huzhugou_page import HuZhuGouPage
from appium import webdriver


class TestMainShoppingFlow:
    def setup(self):
        self.huzhugou = HuZhuGouPage()

    def test_mainshoppingflow(self):
        assert "支付剩余时间" in self.huzhugou.goto_mainshoppingflow().MainShoppingFlow()