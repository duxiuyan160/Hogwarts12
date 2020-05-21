'''
我的页面：
    实现功能：新增收货地址
'''
import re
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from huzhugou_po.page.base_page import BasePage


class AddAddressPage(BasePage):
    _receive_address = (By.XPATH, "//*[@resource-id='com.tojoy.huzhugou:id/iv_util_icon' and @text='收货地址']")  # 收货地址模块
    _btn_add_address = (By.CSS_SELECTOR, ".van-button--normal")  # 添加新地址按钮
    _text_consignee = (By.CSS_SELECTOR, "div:nth-child(1) > .van-cell__value input")  # 收货人（新增收货地址webview页面）
    _text_consignee_phone = (
        By.CSS_SELECTOR, "div:nth-child(2) > .van-cell__value input")  # 收货人联系方式（新增收货地址webview页面）
    _text_consignee_address = (By.CSS_SELECTOR, "div:nth-child(3) > .van-cell__value input")  # 收货人联系地址（新增收货地址webview页面）
    _consignee_address_select = (By.CSS_SELECTOR, ".van-icon-arrow")  # 收货地址选择按钮
    _consignee_address_Provinces = (By.CSS_SELECTOR, ".main-s-a-app>ul:nth-child(1)>li:nth-child(5)")  # 收货地址中省的部分
    _consignee_address_city = (By.CSS_SELECTOR, ".main-s-a-app>ul:nth-child(2)>li:nth-child(10)")  # 收货地址中城市的部分
    _consignee_address_area = (By.CSS_SELECTOR, ".main-s-a-app>ul:nth-child(3)>li:nth-child(10)")  # 收货地址中区的部分
    _consignee_address_county = (By.CSS_SELECTOR, ".main-s-a-app>ul:nth-child(4)>li:nth-child(6)")  # 收货地址中县的部分
    _text_consignee_detailed_address = (
        By.CSS_SELECTOR, "div:nth-child(4) > .van-cell__value input")  # 收货人联系地址（新增收货地址webview页面）
    _btn_consignee_save = (By.CSS_SELECTOR, ".van-button--large")  # 保存按钮（新增收货地址webview页面）
    _list_address_addname = (By.CSS_SELECTOR, ".add-name")  # 收货地址列表中收货人

    # 新增收货地址
    def add_address(self, consignee, consigneephone, consigneeaddress, consigneedetailsaddress):
        self.do_Scroll("收货地址")  # 滑动屏幕至出现收货地址字样
        # 当页面中有android.webkit.WebView出现时，切换上下文，然后进行webview的定位
        WebDriverWait(self.driver, 20).until(lambda x: "WEBVIEW_com.tojoy.huzhugou" in self.driver.contexts)
        self.driver.switch_to.context("WEBVIEW_com.tojoy.huzhugou")
        # *************************************************************************
        self.find(*self._btn_add_address).click()  # 点击添加新地址按钮
        tempconsignee = consignee + str(random.randint(1000, 9999))  # 将测试用例页面传递过来的收货人加上一个4位的随机数赋给一个临时变量
        self.find(*self._text_consignee).send_keys(tempconsignee)  # 收货人框赋值
        self.find(*self._text_consignee_phone).send_keys(consigneephone)  # 收货人联系方式赋值
        self.find(*self._consignee_address_select).click()  # 选择收货地址的选择按钮
        self.find(*self._consignee_address_Provinces).click()  # 选择收货地址的省的部分
        self.find(*self._consignee_address_city).click()  # 选择收货地址的城市的部分
        self.find(*self._consignee_address_area).click()  # 选择收货地址的区的部分
        self.find(*self._consignee_address_county).click()  # 选择收货地址的县的部分
        self.find(*self._text_consignee_detailed_address).send_keys(consigneedetailsaddress)  # 收货人详细地址框赋值
        self.find(*self._btn_consignee_save).click()  # 点击新增收货地址页面的保存按钮

        result = False  # 初始化返回值变量
        namelist = self.finds(*self._list_address_addname)  # 取到收货地址列表中的所有收货人
        for name in namelist:  # 循环判断收货地址列表中的收货人是否有刚新增的收货人，如果有则返回True，否则返回False
            if name.text == tempconsignee:
                result = True
        self.driver.quit()  # 清理环境
        return result

