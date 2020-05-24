from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "emulator-5554"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps['automationName'] = 'UiAutomator2'
        caps["autoGrantPermissions"] = True
        caps["onReset"] = True
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(15)

    # 查找单个元素
    def find(self, by, value):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located((by, value)))
        return self.driver.find_element(by, value)

    # 查找多个元素
    def finds(self, by, value):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located((by, value)))
        return self.driver.find_elements(by, value)

    # find_element_by_android_uiautomator查找元素
    def find_element_by_android_uiautomator(self, locator):
        WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located((MobileBy.ANDROID_UIAUTOMATOR, locator)))
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, locator)