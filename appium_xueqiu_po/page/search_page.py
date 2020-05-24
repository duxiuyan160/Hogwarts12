from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from appium import webdriver
from appium_xueqiu_po.page.base_page import BasePage


class SearchPage(BasePage):
    _text_search_index = (By.ID,"com.xueqiu.android:id/home_search") #主页面的搜索框
    _text_search = (By.ID,"com.xueqiu.android:id/search_input_text") #搜索框
    _select_name = (By.ID,"com.xueqiu.android:id/name") #选择股票
    _btn_add = (By.ID,"com.xueqiu.android:id/follow_btn") #加自选按钮
    _btn_cancle = (By.ID,"action_close") #取消按钮
    _btn_agree = ('new UiSelector().text("同意")')
    _btn_next = ('new UiSelector().textContains("下次再说")')

    def searchkey(self,key,stocktype):
        self.find_element_by_android_uiautomator(self._btn_agree).click() #点击弹出框中的同意按钮
        self.find(*self._text_search_index).click() #点击主页面中的搜索框
        self.find(*self._text_search).click()#点击搜索框
        self.find(*self._text_search).send_keys(key) #查询框赋值
        self.find(*self._select_name).click() #选中查询出来的name的第一个
        #加自选按钮
        _btn_follow = (By.XPATH,
                       "//*[@resource-id='com.xueqiu.android:id/stockCode' and @text='" + stocktype + "']/../../..//*[@resource-id='com.xueqiu.android:id/follow_btn']")
        #已添加按钮
        _btn_followed = (By.XPATH,
                       "//*[@resource-id='com.xueqiu.android:id/stockCode' and @text='" + stocktype + "']/../../..//*[@resource-id='com.xueqiu.android:id/followed_btn']")

        self.find(*_btn_follow).click() #点击加自选按钮
        self.find_element_by_android_uiautomator(self._btn_next).click() #点击弹出框中的下次再说按钮
        _btn_follow_text = self.find(*_btn_followed).text #取到已添加按钮的text
        return _btn_follow_text

