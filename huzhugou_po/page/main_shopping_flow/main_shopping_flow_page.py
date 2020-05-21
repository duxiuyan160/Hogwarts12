"""
主购物流程：
    首页搜索商品->商品展示->商品加入购物车->结算->提交订单
"""
import time
import re

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from huzhugou_po.config.pathconfig import MAIN_SHOPPING_FLOW_DATA_PATH
from huzhugou_po.page.base_page import BasePage


class MainShoppingFlowPage(BasePage):
    _navigation_shop = (By.ID, "com.tojoy.huzhugou:id/navigation_shop")  # 底部导航栏商城按钮
    _btn_Agree = (By.ID, "com.tojoy.huzhugou:id/btn_pos")  # 主页面弹出的条款框中的同意按钮
    _search_main = (By.ID, "com.tojoy.huzhugou:id/search_tv_search")  # 主页面的搜索框
    _search_real = (By.ID, "com.tojoy.huzhugou:id/et_search")  # 点击主页面的搜索框跳转到的搜索框
    _product = (By.ID, "com.tojoy.huzhugou:id/imager")  # 搜到的商品
    _addtocart = (By.ID, "com.tojoy.huzhugou:id/tv_add_to_Cart")  # 加入购物车铵钮
    _btn_cartadd = (By.ID, "com.tojoy.huzhugou:id/button_add")  # 购物车中加数量按钮
    _btn_cartsubmit = (By.ID, "com.tojoy.huzhugou:id/tv_confirm")  # 购物车页面的确定按钮
    _btn_cart = (By.ID, "com.tojoy.huzhugou:id/iv_purchase")  # 购物车按钮
    _btn_Settlement = (By.ID, "com.tojoy.huzhugou:id/Text_total_sku_num")  # 结算按钮
    _btn_submit = (By.ID, "com.tojoy.huzhugou:id/rel_commitOrder")  # 提交按钮
    _pay = (By.ID, "com.tojoy.huzhugou:id/test_Time")  # 订单支付页面的剩余支付时间控件

    # 主购物流
    def MainShoppingFlow(self):
        self.find(*self._navigation_shop).click()  # 点击底部导航栏的商城按钮
        self._testskuname = self.read_yamldata(MAIN_SHOPPING_FLOW_DATA_PATH, "userdata",
                                               "testskuName")  # 获取测试数据：手机号和商品名称

        ##以下是页面行为
        self.find(*self._search_main).click()
        self.find(*self._search_real).click()
        self.find(*self._search_real).send_keys(self._testskuname)  # KJ820F-N800C
        self.driver.press_keycode(66)  # 搜狗键盘上的回车按钮
        self.find(*self._product).click()
        self.find(*self._addtocart).click()  # 点击加入购物车按钮
        for i in range(2):  # 商品加入购物车，数量选2
            self.find(*self._btn_cartadd).click()
        self.find(*self._btn_cartsubmit).click()  # 点击购物车页面的确定按钮
        self.find(*self._btn_cart).click()  # 点击购物车按钮
        self.find(*self._btn_Settlement).click()  # 点击结算按钮
        self.find(*self._btn_submit).click()  # 点击提交按钮
        strpaytip = self.find(*self._pay).text  # 将支付页面的支付信息赋给一个临时变量
        self.driver.quit()  # 清理环境
        return strpaytip
