"""
入口页：
    设置capabilities，并启动
"""
import re
import time
import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
from huzhugou_po.config.pathconfig import MAIN_SHOPPING_FLOW_DATA_PATH
from huzhugou_po.page.base_page import BasePage
from huzhugou_po.page.main_shopping_flow.main_shopping_flow_page import MainShoppingFlowPage
from huzhugou_po.page.my.add_address_page import AddAddressPage


class HuZhuGouPage(BasePage):
    driver = None
    _appPackage = "com.tojoy.huzhugou"  # 包名
    _appActivity = ".activity.WelcomeActivity"  # 初始页面
    _btn_my = (By.ID, "com.tojoy.huzhugou:id/navigation_me")  # 底部导航栏我的按钮
    _btn_Agree = (By.ID, "com.tojoy.huzhugou:id/btn_pos")  # 主页面弹出的条款框中的同意按钮
    _login_phone = (By.ID, "com.tojoy.huzhugou:id/et_mobile")  # 手机号框
    _login_code = (By.ID, "com.tojoy.huzhugou:id/et_code")  # 验证码框
    _btn_getcode = (By.ID, "com.tojoy.huzhugou:id/tv_pull_code")  # 获取验证码按钮
    _getcodetip = ('new UiSelector().className("android.widget.TextView").textContains("【互助购】验证码")')  # 获取桌面通知消息里的验证码信息
    _btn_login = (By.ID, "com.tojoy.huzhugou:id/btn_login")  # 登录按钮

    def first(self):
        # 设置capabilities
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "3HX7N17408005293"
        caps["appPackage"] = self._appPackage
        caps["appActivity"] = self._appActivity
        caps["automationName"] = "UiAutomator2"
        caps["chromedriverExecutable"] = '/Users/duxiuyan/projects/chromedriver/2.43/chromedriver'
        caps["autoGrantPermissions"] = True

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(15)
        HuZhuGouPage.driver = self.driver

    def __init__(self):
        self.first()
        # #如果之前没有启动过app，则调用first方法，否则直接启动页面
        # if HuZhuGouPage.driver == None:
        #     self.first()
        # else:
        #     self.driver.start_activity("com.tojoy.huzhugou",".activity.WelcomeActivity")
        #     #self.driver.start_activity(self.appPackage, self.appActivity)

    # 点击同意按钮
    def click_agree(self):
        self.find(*self._btn_Agree).click()

    # 验证码登录
    def login_by_code(self):
        self.find(*self._btn_my).click()
        self._testphone = self.read_yamldata(MAIN_SHOPPING_FLOW_DATA_PATH, "userdata", "testphone")  # 获取测试手机号
        self.find(*self._login_phone).send_keys(self._testphone)  # 输入一个默认的手机号
        self.find(*self._btn_getcode).click()  # 点击获取验证码按钮
        time.sleep(20)  # 强制等待10，等验证码的出现
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

    # 跳转主流程购物页面
    def goto_mainshoppingflow(self):
        return MainShoppingFlowPage(self.driver)

    # 跳转到我的页面
    def goto_my_add_address(self):
        return AddAddressPage(self.driver)
