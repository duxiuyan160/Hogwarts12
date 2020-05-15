'''
步骤：
1、复用已打开浏览器，取得cookie，并存入json文件中
2、关闭复用模式，读取json文件中的cookie信息，并加入self.driver.add_cookie中
'''
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestWework:
    def setup(self):
        ##复用浏览器
        # option = webdriver.ChromeOptions()
        # option.debugger_address = "127.0.0.1:9999"
        # self.driver = webdriver.Chrome(options=option)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_wework(self):
        ##结合复用的浏览器，取到cookies信息并存入cookies.json文件中
        # json.dump(self.driver.get_cookies(),open("cookies.json","w"),indent=4)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # 读取json文件中的cookies信息
        cookies = json.load(open("cookies.json", "r"))
        # 将cookies中的信息循环加入到self.driver.add_cookie中，并遇到expiry则删除
        for cookie in cookies:
            if "expiry" in cookie:
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        # 刷新当前网页
        self.driver.refresh()
        # 点击通讯录标签
        self.driver.find_element(By.CSS_SELECTOR, "#menu_contacts > span").click()
