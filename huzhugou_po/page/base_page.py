"""
方法封装页：
    封装一些常用的方法，如findelements
"""
import yaml
from selenium.webdriver.remote.webdriver import WebDriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 按普通方式查找元素
    def find(self, by, value):
        WebDriverWait(self.driver, 60).until(expected_conditions.visibility_of_element_located((by, value)))
        return self.driver.find_element(by, value)

    # find_element_by_android_uiautomator查找元素
    def find_element_by_android_uiautomator(self, locator):
        WebDriverWait(self.driver, 40).until(
            expected_conditions.visibility_of_element_located((MobileBy.ANDROID_UIAUTOMATOR, locator)))
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, locator)

    # 读取yaml文件方法
    def read_yamldata(self, filename, section, option1):
        with open(filename, encoding="utf8") as f:
            self.datas = yaml.full_load(f)
            return self.datas[section][option1]
