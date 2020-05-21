'''
前置函数，在测试每个用例页时，都需要实例化driver、点击条款中的同意按钮和验证码登录
'''
import pytest
from selenium.webdriver.common.by import By
from appium import webdriver
from huzhugou_po.page.base_page import BasePage
from huzhugou_po.page.huzhugou_page import HuZhuGouPage


@pytest.fixture("class")
def init_driveranddopre():
    driver = HuZhuGouPage()  # 实例化主向导页面，包含跳转到各个模块和初始化driver
    driver.click_agree()  # 点击条款中的同意按钮
    driver.login_by_code()  # 短信验证码登录
    yield driver  # 返回driver
