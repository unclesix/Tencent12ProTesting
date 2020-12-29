# 删除成员op
from selenium.webdriver.common.by import By

from aWEB.selenium_wxwork_main.po.BasePage import BasePage


# ***继承BasePage构造方法***
class Deletemember(BasePage):

    def deletembrs1(self):
        self.find(By.XPATH,"//input[@id='memberSearchInput']").send_keys("testname")
        self.find(By.XPATH,"//a[@class='qui_btn ww_btn js_del_member']").click()
        self.find(By.XPATH,"//a[@class='qui_btn ww_btn ww_btn_Blue']").click()

    def deletembrs2(self):
        self.find(By.XPATH,"//input[@id='memberSearchInput']").send_keys("testname2")
        self.find(By.XPATH,"//a[@class='qui_btn ww_btn js_del_member']").click()
        self.find(By.XPATH,"//a[@class='qui_btn ww_btn ww_btn_Blue']").click()
