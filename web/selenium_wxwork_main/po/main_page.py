# 1.通过复用技术，访问并扫码登陆企业微信首页。
# 2.在首页中点击 添加成员按钮。并跳转添加成员页面。
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from aWEB.selenium_wxwork_main.po.BasePage import BasePage
from aWEB.selenium_wxwork_main.po.add_members_page import Addmembers
from aWEB.selenium_wxwork_main.po.delete_member_page import Deletemember

#***继承BasePage构造方法***
class Main(BasePage):
    #定义url,否则url为空。
    base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def goto_addmembers(self):
        self.find(By.XPATH,"//a[@id='menu_index']//span[@class='frame_nav_item_title']").click()
        self.find(By.XPATH,"//div[@class='index_service']//a[1]//div[1]//span[2]").click()
        return Addmembers(self.driver)

    def goto_addresslist(self):
        self.find(By.XPATH,"//a[@id='menu_contacts']//span[@class='frame_nav_item_title']").click()
        return Deletemember(self.driver)

    def goto_addresslist2(self):
        self.find(By.XPATH,"//a[@id='menu_contacts']//span[@class='frame_nav_item_title']").click()     #点击通讯录
        #通讯录页面显示等待，添加成员按钮是否可点击。
        self.wait_for_click((By.XPATH,"//div[@class='ww_operationBar']//a[@class='qui_btn ww_btn js_add_member']"))
        self.find(By.XPATH,"//div[@class='ww_operationBar']//a[@class='qui_btn ww_btn js_add_member']").click()
        return Addmembers(self.driver)
