from selenium import webdriver
import os,time

class Base():
    def setup(self):
        browser = os.getenv("browser")          #外部输入
        if browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'PhantomJS':
            self.driver = webdriver.PhantomJS()
        else:
            self.driver = webdriver.Chrome()
        #self.driver.get("https://www.baidu.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()


# windows使用set命令
# set browser=chrome
# pytest XXXX