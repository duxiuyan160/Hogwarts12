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

from huzhugou_po.config.pathconfig import USERCONFIG_FILE_PATH
from huzhugou_po.page.base_page import BasePage


class MainShoppingFlowPage(BasePage):
    _btn_Agree = (By.ID, "com.tojoy.huzhugou:id/btn_pos")  # 主页面弹出的条款框中的同意按钮
    _search_main = (By.ID, "com.tojoy.huzhugou:id/search_tv_search")  # 主页面的搜索框
    _search_real = (By.ID, "com.tojoy.huzhugou:id/et_search")  # 点击主页面的搜索框跳转到的搜索框
    _product = (By.ID, "com.tojoy.huzhugou:id/imager")  # 搜到的商品
    _addtocart = (By.ID, "com.tojoy.huzhugou:id/tv_add_to_Cart")  # 加入购物车铵钮
    _login_phone = (By.ID, "com.tojoy.huzhugou:id/et_mobile")  # 手机号框
    _login_code = (By.ID, "com.tojoy.huzhugou:id/et_code")  # 验证码框
    _btn_getcode = (By.ID, "com.tojoy.huzhugou:id/tv_pull_code")  # 获取验证码按钮
    _getcodetip = ('new UiSelector().className("android.widget.TextView").textContains("【互助购】验证码")')  # 获取桌面通知消息里的验证码信息
    _btn_login = (By.ID, "com.tojoy.huzhugou:id/btn_login")  # 登录按钮
    _btn_cartadd = (By.ID, "com.tojoy.huzhugou:id/button_add")  # 购物车中加数量按钮
    _btn_cartsubmit = (By.ID, "com.tojoy.huzhugou:id/tv_confirm")  # 购物车页面的确定按钮
    _btn_cart = (By.ID, "com.tojoy.huzhugou:id/iv_purchase")  # 购物车按钮
    _btn_Settlement = (By.ID, "com.tojoy.huzhugou:id/Text_total_sku_num")  # 结算按钮
    _btn_submit = (By.ID, "com.tojoy.huzhugou:id/rel_commitOrder")  # 提交按钮

    # 主购物流
    def MainShoppingFlow(self):
        # 先获取测试数据：手机号和商品名称
        self._testphone = self.read_yamldata(USERCONFIG_FILE_PATH, "userdata", "testphone")
        self._testskuname = self.read_yamldata(USERCONFIG_FILE_PATH, "userdata", "testskuName")

        ##以下是页面行为
        self.find(*self._btn_Agree).click()
        self.find(*self._search_main).click()
        self.find(*self._search_real).click()
        self.find(*self._search_real).send_keys(self._testskuname)  # KJ820F-N800C
        self.driver.press_keycode(66)  # 搜狗键盘上的回车按钮
        self.find(*self._product).click()
        self.find(*self._addtocart).click()

        # 验证码登录*******************************************************************
        self.find(*self._login_phone).send_keys(self._testphone)  # 输入一个默认的手机号
        self.find(*self._btn_getcode).click()  # 点击获取验证码按钮
        time.sleep(10)  # 强制等待10，等验证码的出现
        self.driver.open_notifications()  # 打开桌面通知消息框
        time.sleep(3)  # 强制等待3，等验证码的出现

        try:
            codestr = self.find_element_by_android_uiautomator(self._getcodetip).text  # 获取桌面通知消息中的验证码串
            code = re.findall(r'\d+', codestr)[0]  # 用正则取出验证码串中数字部分并转成list，取索引为0的值
            self.driver.keyevent(4)  # 关闭桌面通知消息框
            self.find(*self._login_code).send_keys(code)  # 给验证码框赋值
        except Exception as e:
            raise e
        self.find(*self._btn_login).click()
        # *************************************************************************
        self.find(*self._addtocart).click()  # 点击加入购物车按钮
        for i in range(2):  # 商品加入购物车，数量选2
            self.find(*self._btn_cartadd).click()
        self.find(*self._btn_cartsubmit).click()  # 点击购物车页面的确定按钮
        self.find(*self._btn_cart).click()  # 点击购物车按钮
        self.find(*self._btn_Settlement).click()  # 点击结算按钮
        self.find(*self._btn_submit).click()  # 点击提交按钮
        return self.driver.page_source
