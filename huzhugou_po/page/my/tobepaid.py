'''
待付款页面：
    1、取消订单：点击我的-待付款：
        ->:如果待付款右上角的标没有数字显示，则返回False,并打印没有记录数要操作
        ->:如果待付款右上角的标有数字显示，则先记录操作这前的记录数，然后再取消记录，再用新的记录数+1与操作之前的记录数进行对比，相等返回True,否则返回False
    2、付款 #todo
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.mobile import Mobile
from selenium.webdriver.support.wait import WebDriverWait

from huzhugou_po.page.base_page import BasePage
from appium import webdriver


class ToBePaid(BasePage):
    _number_tobepaid = (By.ID, "com.tojoy.huzhugou:id/tv_num_unpay")  # 待付款的共几条数量
    _btn_tobepaid = ('new UiSelector().className("android.widget.TextView").textContains("待付款")')  # 待付款按钮
    _btn_cancle = (By.CSS_SELECTOR, ".cancel-order>.linkBtn")  # 取消订单按钮(我的订单列表中的第一条)
    _cancle_content = (By.CSS_SELECTOR, ".content")  # 取消订单的标题内容(我的订单列表中的第一条)
    _cancle_reason = (By.CSS_SELECTOR, ".reason-warpper>div:nth-child(1)")  # 取消订单原因
    _btn_cancle_submit = (By.CSS_SELECTOR, ".btn2")  # 取消订单原因的确认按钮
    _btn_back = ("转到上一层级")

    # 取消订单
    def cancle_order(self):
        try:
            old_number_tobepaid = self.find(*self._number_tobepaid).text  # 记录一下取消付款之前，待付款右上角中有几条款操作的记录
        except:
            print("没有可操作的记录")
            self.driver.quit()
            return False

        self.find_element_by_android_uiautomator(self._btn_tobepaid).click()  # 点击我的页面---我的订单---待付款按钮
        # 当页面中有android.webkit.WebView出现时，切换上下文，然后进行webview的定位
        WebDriverWait(self.driver, 20).until(lambda x: "WEBVIEW_com.tojoy.huzhugou" in self.driver.contexts)
        self.driver.switch_to.context("WEBVIEW_com.tojoy.huzhugou")
        self.find(*self._btn_cancle).click()  # 点击取消付款
        self.find(*self._cancle_reason).click()  # 点击我不想买了这个取消原因
        self.find(*self._btn_cancle_submit).click()  # 点击取消原因订单原因页面中的确认按钮
        self.driver.switch_to.context("NATIVE_APP")  # 将上下文切回原生控件
        self.find_element_by_accessibility_id(self._btn_back).click()  # 返回到上一级（从待付款页面返回到我的页面）
        result = False  # 存在结果的临时变量
        try:
            new_number_tobepaid = self.find(*self._number_tobepaid).text  # 再记录一下取消付款后，待付款右上角中有几条款操作的记录
        except:
            new_number_tobepaid = "0"
        if int(old_number_tobepaid) == int(
                new_number_tobepaid) + 1:  # 如果操作完取消付款之后的记录数+1==没操作取消付款之前记录数，则结果返回true，否则false
            result = True
        else:
            result = False
        self.driver.quit()
        return result

    # 付款
    def pay_order(self):
        # todo
        pass
