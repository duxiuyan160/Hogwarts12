'''
执行js脚本
'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestJS:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.baidu.com")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_js(self):
        self.driver.find_element(By.ID,"kw").send_keys("selenium测试")
        ele = self.driver.execute_script("return document.getElementById('su')")
        ele.click()
        self.driver.execute_script("document.documentElement.scrollTop=100000")
        time.sleep(3)