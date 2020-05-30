"""
主页面，进行分管跳转到各个模块
"""
from selenium.webdriver.common.by import By

from appium_xueqiu_po.page.base_page import BasePage
from appium_xueqiu_po.page.market import Market


class Main(BasePage):
    _btn_market = (By.XPATH,'//*[@resource-id="com.xueqiu.android:id/tab_name" and @text="行情"]')

    # 跳转到行情的页面
    def goto_market(self):
        self.click(self.find(*self._btn_market))
        return Market(self._driver)