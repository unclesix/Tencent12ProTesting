#从通讯录入口添加成员，测试用例
import time

from aWEB.selenium_wxwork_main.po.main_page import Main


class Testaddress_addmbs:
    def setup(self):
        # 初始化Main，会先调用公共构造方法
        self.main = Main()

    def test_addressaddmbs(self):
        addmember = self.main.goto_addresslist2()
        addmember.add_members2()
        assert addmember.get_members("testname2")

    def test_deletembs(self):
        self.main.goto_addresslist().deletembrs2()
        assert True