from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from appium import webdriver
from appium_xueqiu_po.page.base_page import BasePage


class SearchPage(BasePage):
    _text_search_market = (By.ID, "com.xueqiu.android:id/action_search")  # 行情页面的搜索框
    _text_search = (By.ID, "com.xueqiu.android:id/search_input_text")  # 搜索框
    _select_name = (By.ID, "com.xueqiu.android:id/name")  # 选择股票
    _btn_add = (By.ID, "com.xueqiu.android:id/follow_btn")  # 加自选按钮
    _btn_next = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("下次再说")')

    def searchkey(self, key, stocktype):
        self.click(self.find(*self._text_search_market))  # 点击主页面中的搜索框
        self.click(self.find(*self._text_search))  # 点击搜索框
        self.find(*self._text_search).send_keys(key)  # 查询框赋值
        self.click(self.find(*self._select_name))  # 选中查询出来的name的第一个
        # 加自选按钮
        _btn_follow = (By.XPATH,
                       "//*[@resource-id='com.xueqiu.android:id/stockCode' and @text='" + stocktype + "']/../../..//*[@resource-id='com.xueqiu.android:id/follow_btn']")
        # 已添加按钮
        _btn_followed = (By.XPATH,
                         "//*[@resource-id='com.xueqiu.android:id/stockCode' and @text='" + stocktype + "']/../../..//*[@resource-id='com.xueqiu.android:id/followed_btn']")

        self.click(self.find(*_btn_follow))  # 点击加自选按钮
        self.click(self.find(*self._btn_next))
        _btn_follow_text = self.find(*_btn_followed).text  # 取到已添加按钮的text
        return _btn_follow_text
