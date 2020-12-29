# 使用pageobjec原则，对百度搜索内容进行封装
from selenium import webdriver
import pytest, time

# from aWEB.pageobject2 import Main2


class Main:
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_gotobaidu(self):
        driver = self.driver
        driver.get("https://www.baidu.com")
        driver.find_element_by_xpath("//*[@id='kw']").send_keys("霍格沃兹测试学院")
        driver.find_element_by_xpath("//*[@id='su']").click()

    def test_get_firstlink(self):
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='1']/h3/a").click()
        time.sleep(2)
        #当点击链接进入“霍格沃兹测试学院”页面，那么直接return跳到Main2这个实例中。其中包括了Main中对“霍格沃兹测试学院”的一些方法
        from aWEB.selenium_po.pageobject2 import Main2
        return Main2()

if __name__ == '__main__':
    pytest.main()