# # 一、浏览器复用： 1.使用调试模式打开企业微信并登陆，获取cookie并使用shelve数据库保存。
# #             2.保存后生成cookie.bak、cookie.dat、cookie.dir三个文件。
#
# import shelve
# import time
#
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
#
# class Testchrome():
#     def setup_method(self):
#         #浏览器复用：使用Options方法，与已打开的chrome端口进行链接，这里可以理解为电话的另一端。
#         options = Options()
#         options.debugger_address = "127.0.0.1:9222"
#         self.driver = webdriver.Chrome(options=options)
#
#     def teardown_method(self):
#         self.driver.quit()
#
#     def test_demo2(self):
#         db = shelve.open("D:\\mylearntest\\aWEB\\selenium_cookie\\cookie")
#         db['cookie'] = self.driver.get_cookies()
#         #提取db为cookie的文件数据
#         cookies = db['cookie']
#         #在企业微信登陆后页面，使用webdriver  get_cookies方法直接过滤获取cookie
#         print(self.driver.get_cookies())
#
#         #记得关闭db
#         db.close()



# 二、浏览器复用：通过获取的cookie信息，即使不适用chrome调试，也可以实现登陆。

import shelve
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class Testchrome():
    def setup_method(self):
        #浏览器复用：使用Options方法，与已打开的chrome端口进行链接，这里可以理解为电话的另一端。
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        #取消复用
        self.driver = webdriver.Chrome()



    def teardown_method(self):
        self.driver.quit()

    def test_demo2(self):
        #加入cookies，必须要先访问页面,才能实现cookie的加入，比如访问首页
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        db = shelve.open("D:\\mylearntest\\aWEB\\selenium_cookie\\cookie")
        #提取db为cookie的文件数据
        cookies = db['cookie']

        # #循环加入每个cookie,
        for cookie in cookies:

            #如果expiry参数在cookie中，则使用pop方法删除。再次打开一个窗口登陆
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)

        #加入cookies后，再进行一个访问
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        time.sleep(2)

        #点击通讯录按钮
        self.driver.find_element_by_xpath("//*[@id='menu_contacts']").click()
        time.sleep(2)

        #记得关闭db
        db.close()



