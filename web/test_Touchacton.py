from selenium import webdriver
import pytest,time
from selenium.webdriver import TouchActions


class Testtouchaction():
    def setup(self):
        #配置 chrome 启动属性的类。
        option = webdriver.ChromeOptions()
        #添加实验性质的设置参数 (add_experimental_option)
        option.add_experimental_option('w3c',False)
        #引用设置后的属性类
        self.driver = webdriver.Chrome(chrome_options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()

    def test_touchaction_scrollbottom(self):
        self.driver.get("https://www.baidu.com")
        el = self.driver.find_element_by_id("kw")
        el_search = self.driver.find_element_by_id("su")

        el.send_keys("seleniumceshi")
        action = TouchActions(self.driver)
        action.tap(el_search)   #tap模拟敲击操作
        action.perform()
        # scroll_from_element ：以输入框为初始位置，x=0，y=10000，滑动在最底部，perform方法执行
        # 此处需要配置chrome启动属性的类。不然会报错
        action.scroll_from_element(el,0,10000).perform()
        time.sleep(3)