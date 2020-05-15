'''
测试案例：
1、打开网页"https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
2、操作窖口右侧页面，将元素1拖拽到元素2
3、这时候会有一个alert弹框，点击弹框中的"确定"
4、然后再按"点击运行"
5、关闭网页
'''
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestAlert:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_alert(self):
        self.driver.switch_to_frame("iframeResult")
        ele_drag = self.driver.find_element(By.ID,"draggable")
        ele_drop = self.driver.find_element(By.ID,"droppable")

        action = ActionChains(self.driver)
        action.drag_and_drop(ele_drag,ele_drop).perform()
        sleep(2)

        self.driver.switch_to.alert.accept()
        self.driver.switch_to.default_content()
        sleep(3)