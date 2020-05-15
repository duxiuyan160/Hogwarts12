'''
测试案例一：
    1）打开页面（https://sahitest.com/demo/clicks.htm）
    2）分别对按钮'click me','dbl click me','right click me'，执行点击，双击，右键操作
    3）打印上面展示框中的内容

测试案例二：movetoelement
测试案例三：dragdrop

'''
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestActionChains:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        #self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    #单击、右击、双击
    def test_actionchains(self):
        self.driver.get("https://sahitest.com/demo/clicks.htm")
        element_click = self.driver.find_element(By.XPATH,"//input[@value='click me']")
        element_doubleclick = self.driver.find_element(By.XPATH,"//input[@value='dbl click me']")
        element_rightclick = self.driver.find_element(By.XPATH,"//input[@value='right click me']")

        action = ActionChains(self.driver)
        action.click(element_click)
        action.context_click(element_doubleclick)
        action.double_click(element_doubleclick)
        action.perform()
    #移动
    def test_movetoelement(self):
        self.driver.get("http://www.baidu.com")
        sleep(3)
        #ele = self.driver.find_element(By.NAME,"tj_settingicon")
        ele = self.driver.find_element(By.LINK_TEXT, "更多")
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        sleep(3)

    #拖拽
    def test_dragdrop(self):
        self.driver.get("")
        drag_ele = self.driver.find_element(By.ID,"dragger")
        drop_ele = self.driver.find_element(By.XPATH,"/html/body/div[2]")
        action = ActionChains(self.driver)
        #action.drag_and_drop(drag_ele,drop_ele)
        action.click_and_hold(drag_ele).release(drop_ele).perform()
        action.click_and_hold(drag_ele).move_to_element(drop_ele).release().perform()

    #键盘输入事件
    def test_keys(self):
        self.driver.get("http:sahitest.com/demo/label.htm")
        ele = self.driver.find_element(By.XPATH,"")
        ele.click()

        action = ActionChains(self.driver)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE)
        action.send_keys("tom")
        action.send_keys(Keys.BACK_SPACE).perform()


