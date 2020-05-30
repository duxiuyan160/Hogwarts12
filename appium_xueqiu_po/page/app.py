from appium import webdriver

from appium_xueqiu_po.page.base_page import BasePage
from appium_xueqiu_po.page.main import Main


class App(BasePage):
    _appPackage = "com.xueqiu.android"  # 包名
    _appActivity = ".view.WelcomeActivityAlias"  # 初始页面


    def start(self):
        if self._driver is None:
            caps = dict()
            caps["platformName"] = "android"
            caps["deviceName"] = "3HX7N17408005293"
            caps["appPackage"] = self._appPackage
            caps["appActivity"] = self._appActivity
            caps["automationName"] = "UiAutomator2"
            caps["chromedriverExecutable"] = '/Users/duxiuyan/projects/chromedriver/2.43/chromedriver'
            caps["autoGrantPermissions"] = True
            caps["noReset"] = True

            self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        else:
            self._driver.start_activity(self._appPackage, self._appActivity)
        self._driver.implicitly_wait(15)
        return self

    # 跳转至主页面
    def main(self) -> Main:
        return Main(self._driver)
