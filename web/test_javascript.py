from aWEB.base import Base
import time
import pytest
class TestJS(Base):
    @pytest.mark.skip
    def test_js_scroll(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys("selenium测试")
        #self.driver.find_element_by_xpath('//*[@id="su"]').click()
        element = self.driver.execute_script('return document.getElementById("su")')
        time.sleep(2)
        element.click()
        jsscorll = ("document.documentElement.scrollTop='10000'")
        self.driver.execute_script(jsscorll)
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[@class='n']").click()
        time.sleep(2)

        #将js数据返回，以便分析
        #方式一
        # for code in ['\n return document.title',
        #              'return JSON.stringify(performance.timing)']:
        #     print(self.driver.execute_script(code))
        #方式二,此方式虽然是合并打印，但是只会打印第一个js语句
        # print(self.driver.execute_script(
        #              'return document.title',
        #              'return JSON.stringify(performance.timing)')
        #                                 )

    def test_datetime(self):
        self.driver.get("https://www.12306.cn/index/")
        for readonly1 in["a=document.getElementById('train_date')",
                         "a.removeAttribute('readonly')",
                         "document.getElementById('train_date').value='2020-08-24'",
                         'return document.getElementById("train_date").value']:
            print(self.driver.execute_script(readonly1))
        time.sleep(5)
        # self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        # self.driver.execute_script("document.getElementById('train_date').value='2020-08-24'")
