from selenium.webdriver import ActionChains

from web.base import Base
import time,pytest

class Testupfile(Base):
    #文件上传send_keys方式
    @pytest.mark.skip
    def test_upfile(self):
        self.driver.get("https://image.baidu.com/")
        #点击相机按钮
        self.driver.find_element_by_xpath("//*[@id='sttb']/img[1]").click()
        self.driver.find_element_by_id("stfile").send_keys("D:\\mylearntest\\datas\\testupfile.jpg")
        time.sleep(5)

    #处理alert弹窗
    def test_alertdeal(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to_frame("iframeResult")

        el1 = self.driver.find_element_by_id("draggable")
        el2 = self.driver.find_element_by_id("droppable")
        action= ActionChains(self.driver)
        action.drag_and_drop(el1,el2).perform()

        #切换到alert上，并点击确认:
        # switch_to_alert() 和 switch_to_default_content() 3.8不识别。无法使用
        self.driver.switch_to.alert.accept()

        time.sleep(3)
        #切换并返回默认的frame下
        self.driver.switch_to.default_content()
        time.sleep(3)
        #点击“运行”按钮
        self.driver.find_element_by_id("submitBTN").click()
        time.sleep(2)
