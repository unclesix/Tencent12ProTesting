# 1.C:\Users\dell>chrome --remote-debugging-port=9222     【chrome单步调试】
# 2.打开的chrome，手动打开https://ceshiren.com/，且停留在当前页面。
# 3.执行test_chromefuyong.py，会直接在当前登陆页面进行操作。

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class Testchrome():
    def setup_method(self):
        #使用Options方法，与已打开的chrome端口进行链接，这里可以理解为电话的另一端。
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)

    def teardown_method(self):
        self.driver.quit()

    def test_demo(self):
        #不需要再进行访问链接，直接可以通过已打开的9222端口的chrome进行点击。
        #self.driver.get("https://ceshiren.com/")
        self.driver.find_element(By.LINK_TEXT, "所有分类").click()
        time.sleep(5)