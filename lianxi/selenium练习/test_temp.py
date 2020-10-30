
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestTemp:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://signup.jp.leagueoflegends.com/ja/signup/index#/")
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_temp(self):
        self.driver.find_element(By.NAME,"email").send_keys("chengqing@163.com")
        self.driver.find_element(By.NAME,"username").send_keys("chengqing1")
        self.driver.find_element(By.NAME,"password").send_keys("qing-123")
        self.driver.find_element(By.NAME,"confirm_password").send_keys("qing-123")
        self.driver.find_element(By.CSS_SELECTOR,".next-button").click()

        sleep(3)