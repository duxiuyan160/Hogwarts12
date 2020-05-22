import pytest
import yaml

from huzhugou_po.config.pathconfig import BASE_DIR, ADD_ADDRESS_DATA_PATH
from huzhugou_po.page.huzhugou_page import HuZhuGouPage
from appium import webdriver


@pytest.mark.usefixtures("init_driver")
class TestAddAddress:

    @pytest.mark.parametrize("consigneedata", yaml.safe_load(open(ADD_ADDRESS_DATA_PATH)))
    def test_add_address(self, init_driver, consigneedata):
        '''执行用例：新增收货地址，并断言新增的收货人是否在收货地址列表中'''
        consignee = consigneedata["consignee"]  # 获取收货人测试数据
        consigneephone = consigneedata["consigneephone"]  # 获取收货人联系方式测试数据
        consigneeaddress = consigneedata["consigneeaddress"]  # 获取收货人地址测试数据
        consigneedetailsaddress = consigneedata["consigneedetailsaddress"]  # 获取收货人详细地址测试数据
        assert HuZhuGouPage.goto_my_add_address(init_driver).add_address(consignee, consigneephone,
                                                                                 consigneeaddress,
                                                                                 consigneedetailsaddress) == True
