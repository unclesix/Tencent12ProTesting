from selenium import webdriver
from selenium.webdriver import ActionChains
import pytest,time
from selenium.webdriver.common.keys import Keys


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    #使用ActionChains模拟鼠标点击
    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        element_click = self.driver.find_element_by_xpath("//input[@value='click me']")
        element_doubleclick = self.driver.find_element_by_xpath("//input[@value='dbl click me']")
        element_rigthclick = self.driver.find_element_by_xpath("//input[@value='right click me']")
        #使用ActionChains方法调用，并传入driver
        action = ActionChains(self.driver)
        action.click(element_click)
        action.double_click(element_doubleclick)
        action.context_click(element_rigthclick)
        #将执行放入perform队列
        action.perform()
        time.sleep(3)

    @pytest.mark.skip
    #移动鼠标  move_to_element
    def test_moveto(self):
        self.driver.get("https://www.baidu.com")
        moveto = self.driver.find_element_by_xpath("//*[@id='s-usersetting-top']")
        action = ActionChains(self.driver)
        action.move_to_element(moveto)
        action.perform()
        time.sleep(3)

    @pytest.mark.skip
    #鼠标拖拽 drag_and_drop
    def test_dragdrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        # 拖住要移动的元素
        dragdrop_element = self.driver.find_element_by_id("dragger")
        # 放到目标位置并释放
        drop_element = self.driver.find_element_by_xpath("/html/body/div[3]")
        action = ActionChains(self.driver)
        #方法一：
        # action.drag_and_drop(dragdrop_element,drop_element)
        #方法二：点击并按住第一个元素，放到release中释放
        # action.click_and_hold(dragdrop_element).release(drop_element)
        # action.perform()
        #方法三：
        action.click_and_hold(dragdrop_element).move_to_element(drop_element).release().perform()
        time.sleep(3)

    #模拟按键   send_keys用法 ，关联Keys类，【Keys需要导入from selenium.webdriver.common.keys import Keys】具体使用查看。
    def test_sendkeys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele = self.driver.find_element_by_xpath("/html/body/label[1]/input")
        ele.click()                                 #点击输入框
        action = ActionChains(self.driver)
        action.send_keys("username").pause(1)       #.pause(1)  每个操作间隔1秒
        action.send_keys(Keys.SPACE).pause(1)       #空格
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).perform() #删除一个字符
        time.sleep(3)

if __name__ == '__main__':
    pytest.main('-v','-s')