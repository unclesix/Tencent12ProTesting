import selenium
from selenium import webdriver
from aWEB.base import Base


class Testfrmae(Base):
    def test_selenium(self):
        self.driver.get("https://www.baidu.com")
        print("hello")
