import pytest

from huzhugou_po.page.huzhugou_page import HuZhuGouPage


@pytest.mark.usefixtures("init_driver")
class TestToBePaid:
    #执行我的->待付款->取消订单的测试用例
    def test_cancel_order(self,init_driver):
        assert HuZhuGouPage.goto_my_tobepaid(init_driver).cancle_order() == True

    #执行我的->待付款->付款的测试用例
    def test_pay_order(self):
        #todo
        pass
