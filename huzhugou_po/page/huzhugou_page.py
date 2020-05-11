"""
入口页：
    设置capabilities，并启动
"""
from appium import webdriver
from selenium.webdriver.common.by import By
from huzhugou_po.page.base_page import BasePage
from huzhugou_po.page.main_shopping_flow.main_shopping_flow_page import MainShoppingFlowPage


class HuZhuGouPage(BasePage):
    driver = None
    appPackage = "com.tojoy.huzhugou"  # 包名
    appActivity = ".activity.WelcomeActivity"  # 初始页面

    def first(self):
        #设置capabilities
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "3HX7N17408005293"
        caps["appPackage"] = self.appPackage
        caps["appActivity"] = self.appActivity
        caps["automationName"] = "UiAutomator2"
        caps["autoGrantPermissions"] = True

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(15)
        HuZhuGouPage.driver = self.driver

    def __init__(self):
        #self.first()
        #如果之前没有启动过app，则调用first方法，否则直接启动页面
        if HuZhuGouPage.driver == None:
            self.first()
        else:
            self.driver.start_activity(self.appPackage,self.appActivity)
    #跳转主流程购物页面
    def goto_mainshoppingflow(self):
        return MainShoppingFlowPage(self.driver)