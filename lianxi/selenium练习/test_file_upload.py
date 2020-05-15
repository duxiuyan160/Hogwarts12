from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestFileUpload:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://image.baidu.com")
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_file_upload(self):
        self.driver.find_element(By.CSS_SELECTOR,"#sttb > img.st_camera_off").click()
        self.driver.find_element(By.ID,"stfile").send_keys("/Users/duxiuyan/Desktop/1589360933967.jpg")
        sleep(3)

