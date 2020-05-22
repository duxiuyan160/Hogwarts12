from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class WeworkMain:
    def __init__(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self._driver = webdriver.Chrome(options=options)
        self._driver.get('https://work.weixin.qq.com/wework_admin/frame')
