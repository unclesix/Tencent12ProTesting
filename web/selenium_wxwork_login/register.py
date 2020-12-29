#注册页面po
import time

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class Register:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.driver.implicitly_wait(5)

    def register_sends(self):
        self.driver.find_element_by_xpath("//input[@id='corp_name']").send_keys("企业名称-注册测试")
        self.driver.find_element_by_xpath("//a[@class='qui_btn ww_btn ww_btn_Big ww_btn_Block ww_btn_Dropdown js_corp_industry_btn']").click()
        self.driver.find_element_by_xpath("//a[contains(text(),'IT')]").click()
        self.driver.find_element_by_xpath("//div[@class='qui_dropdownMenu ww_dropdownMenu js_corp_industry_ul register_corp_industry_ul register_corp_industry_ul_Two']//div[1]//div[1]//a[1]").click()
        self.driver.find_element_by_xpath("//input[@id='register_tel']").send_keys("13287763693")
        time.sleep(4)
        self.driver.quit()
        return True