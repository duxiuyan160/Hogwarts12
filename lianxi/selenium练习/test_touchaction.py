'''
案例1：
1、打开Chrome
2、打开URL：http://www.baidu.com
3、向搜索框中输入'selenium测试'
4、通过TouchAction点击搜索框
5、滑动到底部，点击下一页
6、关闭Chrome
'''
from time import sleep

from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By


class TestTouchAction:
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option("w3c",False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.get("http://www.baidu.com")
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_touchaction(self):
        ele = self.driver.find_element(By.ID,"kw")
        ele_search = self.driver.find_element(By.ID,"su")
        ele.click()
        ele.send_keys("selenium测试")

        action = TouchActions(self.driver)
        action.tap(ele_search)
        action.perform()

        action.scroll_from_element(ele_search,2,10000).perform()
        sleep(3)




