#登陆页面po

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver     #driver: WebDriver 导入的。alt+enter

from aWEB.selenium_wxwork_login.register import Register


class Login:
    #复用 WebDriver.   "driver:" 意思是指定driver运行的类型是WebDriver，可以使用WebDriver的方法
    def __init__(self,driver: WebDriver):
        self.driver = driver

    def scanf(self):   #扫码登陆，pass
        pass

    def goto_register(self):
        self.driver.find_element_by_xpath("//a[@class='login_registerBar_link']").click()
        return Register(self.driver)    #***因为需要复用driver，所以此时return要传入self.driver***



