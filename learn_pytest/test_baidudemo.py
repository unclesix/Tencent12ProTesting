import allure,pytest
import time
from selenium import webdriver

@allure.testcase("http://github.com")
@allure.feature("百度搜索demo")
@pytest.mark.parametrize("test_dates1",["allure","pytest","unittest"])
def test_steps_demo(test_dates1):
    with allure.step("第一步：打开百度首页"):
        dirver = webdriver.Chrome()
        dirver.maximize_window()
        dirver.get("https://www.baidu.com")

    with allure.step("第二步：将搜索值传入输入框：{}".format(test_dates1)):
        dirver.find_element_by_id("kw").send_keys(test_dates1)
        time.sleep(2)
        dirver.find_element_by_id("su").click()
        time.sleep(2)

    with allure.step("第三步：将图片截图并传入报告中"):
        dirver.save_screenshot("./result/baidu.jpg")
        allure.attach.file("./result/baidu.jpg",attachment_type = allure.attachment_type.JPG)

    with allure.step("第四步：退出浏览器"):
        dirver.close()


