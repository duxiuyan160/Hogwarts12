import pytest

from huzhugou_po.page.huzhugou_page import HuZhuGouPage
from appium import webdriver


@pytest.mark.usefixtures("init_driveranddopre")
class TestMainShoppingFlow:

    # 执行用例：验证码登录->首页搜索商品->商品展示->商品加入购物车->结算->提交订单，并断言
    def test_mainshoppingflow(self, init_driveranddopre):
        assert "支付剩余时间" in HuZhuGouPage.goto_mainshoppingflow(init_driveranddopre).MainShoppingFlow()
