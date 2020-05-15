'''
测试案例
1、打开百度页面
2、点击登录
3、弹框中点击"立即注册"，输入用户名和帐号
4、返回刚才的登录页，点击登录
5、输入用户名和密码，点击登录
'''
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestFrame:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.baidu.com")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_frame(self):
        self.driver.find_element(By.XPATH,'//*[@id="u1"]/a[2]').click()
        self.driver.find_element(By.XPATH,"//div/a[@class='pass-reglink pass-link']").click()

        window = self.driver.current_window_handle

        self.driver.switch_to_window(self.driver.window_handles[-1])#切换到最后一个窗口
        self.driver.find_element(By.NAME,"userName").send_keys("username")

        self.driver.switch_to_window(window)


        self.driver.find_element(By.XPATH,"//div/p[@class='tang-pass-footerBarULogin pass-link']").click()

        sleep(3)

