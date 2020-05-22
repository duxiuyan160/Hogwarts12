'''
前置函数：
1、init_driver：只实例化webdriver
2、init_driveranddopre：第一个测试的测试用例需要调用此函数,后面的操作不要在会话前重置应用状态
'''
import pytest
from selenium.webdriver.common.by import By
from appium import webdriver
from huzhugou_po.page.base_page import BasePage
from huzhugou_po.page.huzhugou_page import HuZhuGouPage


@pytest.fixture("class")
def init_driver():
    '''只实例化webdriver'''
    driver = HuZhuGouPage()  # 实例化主向导页面，包含跳转到各个模块和初始化driver
    yield driver  # 返回driver

@pytest.fixture("class")
def init_driveranddopre():
    '''实例化webdriver,第一个测试的用例中调用此函数'''
    driver = HuZhuGouPage()  # 实例化主向导页面，包含跳转到各个模块和初始化driver
    driver.click_agree()  # 点击条款中的同意按钮
    driver.login_by_code()  # 短信验证码登录
    yield driver  # 返回driver
