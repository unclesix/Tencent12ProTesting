# 初始脚本：1.初始化访问  2.点击跳转登陆页面，return到登录页  3.点击跳转注册页面，return到注册页

from selenium import webdriver

from aWEB.selenium_wxwork_login.login import Login
from aWEB.selenium_wxwork_login.register import Register

class Index:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")

    def goto_login(self):
        self.driver.find_element_by_xpath("//a[@class='index_top_operation_loginBtn']").click()
        return Login(self.driver)   #***因为需要复用driver，所以此时return要传入self.driver***

    def goto_register_hpage(self):
        self.driver.find_element_by_xpath("//a[@class='index_head_info_pCDownloadBtn']").click()
        return Register(self.driver)    #***因为需要复用driver，所以此时return要传入self.driver***

