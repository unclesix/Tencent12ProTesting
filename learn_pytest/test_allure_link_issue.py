import allure


# # 加link 链接
# @allure.link("https://www.baidu.com/",name="链接百度")
# def test_link():
#     print("将测试结果链接至 测试管理系统")
#     pass


#把一条测试用例链接到对应管理的网站上
TEST_CASE_LINK = 'https://github.com/qameta/allure-integrations/issues/8#issuecomment-268313637'
@allure.testcase(TEST_CASE_LINK,'登录用例')
def test_with_testcase_link():
    print("这是一跳测试用例的链接，链接到测试用还在里面")
    pass