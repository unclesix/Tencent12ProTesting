
import allure

from unittest import TestCase
from web.selenium_jenkins_api.library.httpclient import HttpClient
import json

@allure.feature('Test Weater api')
class Weather(TestCase):

    def setUp(self):
        #此处的setUp是当前文件的初始化动作，但是Wwather继承了TestCase类，TestCase本身及父类、父类的父类都会存在Setup。所以需要先运行一下前置的setup。
        #此处不写super().setup()对于当前文件没有影响。
        super().setUp()
        self.host = 'https://api.apiopen.top/videoCategory'
        self.cleint = HttpClient()

    @allure.story ('Test of shenghuo')
    def test_1(self):
        title = '#生活'
        itemid = '36'
        id = 0
        self._test(title,itemid,id)

    @allure.story('Test of donghua')
    def test_2(self):
        title = '#动画'
        itemid = '10'
        id = 1
        self._test(title,itemid,id)

    @allure.story('Test of gaoxiao')
    def test_3(self):
        title = '#搞笑'
        itemid = '28'
        id = 2
        self._test(title,itemid,id)

    def _test(self, title,itemid,id):
        url = 'https://api.apiopen.top/videoCategory'
        response = self.cleint.Get(url = url)
        # 因每个data分为多个数组，此处使用标识来区分每个test。id定义从0开始。  while 循环请求并断言
        act_title = response.json()['result']['itemList'][id]['data']['title']
        print(f'Expect title = {act_title}, while actual title = {title}')
        self.assertEqual(act_title,title, f'Expect title = {act_title}，while actual title = {itemid}')

