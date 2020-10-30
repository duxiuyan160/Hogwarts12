from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.extensions.android.gsm import GsmCallActions


class TestJiaoHu:
    def setup(self):
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

    def teardonw(self):
        pass

    def test_mobile(self):
        self.driver.start_recording_screen()#录屏，8.0以上支持，华为不支持
        self.driver.make_gsm_call("13812345678", GsmCallActions.CALL)  # 模拟打电话
        self.driver.send_sms("13812345671", "hello")  # 模拟发送短信
        self.driver.set_network_connection(1)  # 连网类型
        self.driver.get_screenshot_as_file("./photos/img.png")  # 截图
        self.driver.stop_recording_screen() #录屏结束
