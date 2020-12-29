from aWEB.base import Base

class Testframe(Base):
    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        #进入frame中
        self.driver.switch_to.frame("iframeResult")
        #打印frame中的“请拖拽我”
        print(self.driver.find_element_by_id("droppable").text)

        #切换回默认的frame中
        # self.driver.switch_to.parent_frame()        #方式一，父级frame
        self.driver.switch_to_default_content()     #方式二，默认frame
        print(self.driver.find_element_by_id("submitBTN").text)