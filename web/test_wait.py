from selenium import webdriver
import time

class Testwait():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://ceshiren.com/")

    def test_wait(self):
        #self.driver.find_element_by_xpath('//*[@id="ember35"]//a').click()
        self.driver.find_element_by_xpath("//li[@id='ember35']//a").click()
        time.sleep(3)
        print("进入热门模块")
        self.driver.find_element_by_xpath("html/body/section/div/div[2]/div[5]/div[2]/div/div/div[2]/table/tbody/tr[5]/td[1]/span/a").click()

    def teardown(self):
        self.driver.close()
