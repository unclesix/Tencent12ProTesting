# 对添加成员页面进行封装。
import time

from selenium.webdriver.common.by import By

from web.selenium_wxwork_main.po.BasePage import BasePage


# ***继承BasePage构造方法***
class Addmembers(BasePage):

    # 从首页点击添加成员
    def add_members(self):
        self.find(By.ID,"username").send_keys("testname")
        self.find(By.ID,"memberAdd_acctid").send_keys("1testacctid")
        self.find(By.ID,"memberAdd_phone").send_keys("13287766666")
        self.find(By.XPATH,"//div[@class='member_edit']//div[3]//a[2]").click()


    # 从通讯录中点击添加成员
    def add_members2(self):
        self.find(By.ID,"username").send_keys("testname2")
        self.find(By.ID,"memberAdd_acctid").send_keys("testacctid3")
        self.find(By.ID,"memberAdd_phone").send_keys("13287777777")
        self.find(By.XPATH,"//div[@class='member_edit']//div[3]//a[2]").click()


    # 【优化版】分页索引，为测试用例断言提供封装方法：
    def page_update(self):
        #获取分页信息 1/10，将list进行以“/”号进行1次切割。  [1/10]   0=1/1=10，赋值到page=1，totle=10；     并将str类型转换成int类型
        content: str = self.driver.find_element(By.CSS_SELECTOR,".ww_pageNav_info_text").text
        return [int(i) for i in content.split('/',1)]

    # 根据css元素获取所有姓名。注意此时用的是“elements”
    # 定义一个value变量
    def get_members(self,value):
        #***添加用户完成后，页面有个加载时间，如果不设置等待，则会直接报错。所以可以根据勾选框是否可点击来判断页面是否完成加载。（因为勾选框渲染加载较慢）*** 【旁敲侧击法】
        self.wait_for_click((By.CSS_SELECTOR,'.ww_checkbox'))

        #分页索引，为测试用例断言提供封装方法：
        #调用切割方法，并赋值page, totle_page，判断获取的值是否等于value。【测试用例中赋值】，如果等于，则停留当前页面。
        page, totle_page = self.page_update()
        while True:
            elements = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')  #姓名列表
            for element in elements:
                if value == element.get_attribute("title"):
                    return True

            # 刷新当前页，判断当前页是否等于总页数。是，则退出列表。不是则点击>下一页。
            page = self.page_update()[0]
            if page == totle_page:
                return False
            self.driver.find_element(By.CSS_SELECTOR,'.js_next_page').click()




