# 测试脚本，开启复用浏览器，并调用封装的 ，mainpage和addmembers page
import time
import pytest

from web.selenium_wxwork_main.po.main_page import Main


class Testaddmembers:
    def setup(self):
        self.main = Main()

    def test_addmembers(self):
        # self.main.goto_addmembers().add_members()
        addmember = self.main.goto_addmembers()
        addmember.add_members()
        assert addmember.get_members('ftest')

    # @pytest.mark.skip
    def test_deletembs(self):
        self.main.goto_addresslist().deletembrs1()
        assert True
