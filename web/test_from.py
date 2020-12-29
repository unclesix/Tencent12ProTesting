from selenium import webdriver
import pytest,time
from selenium.webdriver import TouchActions

class Testfrom():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()

    def test_from(self):
        self.driver.get("https://testerhome.com/account/sign_in")
        self.driver.find_element_by_id("user_login").clear()
        self.driver.find_element_by_id("user_password").clear()
        self.driver.find_element_by_id("user_login").send_keys("3176705297@qq.com")
        self.driver.find_element_by_id("user_password").send_keys("1993413")
        #勾选记住密码
        self.driver.find_element_by_id("user_remember_me").click()
        self.driver.find_element_by_xpath("//*[@id='new_user']/div[4]/input").click()
        time.sleep(3)