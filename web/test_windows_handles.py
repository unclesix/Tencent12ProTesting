from selenium import webdriver
import time
from aWEB.base import Base

class Testwindos(Base):
    def test_windows(self):
        self.driver.get("https://www.baidu.com")
        # h1 = self.driver.window_handles
        # print(h1)
        self.driver.find_element_by_xpath('//*[@id="u1"]/a[2]').click()    #点击登陆按钮
        self.driver.find_element_by_xpath('//*[@id="passport-login-pop-dialog"]/div/div/div/div[3]/a').click()  #点击注册按钮，新建一个窗口
        #查看所有句柄
        windows = self.driver.window_handles

        #切换注册页面的句柄, 从后往前截取
        self.driver.switch_to_window(windows[-1])
        self.driver.find_element_by_id('TANGRAM__PSP_4__userName').send_keys("username")
        time.sleep(3)

        #切换回登陆页面
        #self.driver.switch_to_window(self.driver.window_handles[0])
        self.driver.switch_to_window(windows[0])
        self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()
        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("波比波比hong")
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys("1993413")
        self.driver.find_element_by_id("TANGRAM__PSP_11__submit").click()
        time.sleep(3)





