
import allure

from unittest import TestCase
from web.selenium_jenkins_api.library.httpclient import HttpClient
import json

@allure.feature('Test Weater api')
class Weather(TestCase):

    def setUp(self):

        self.host = 'https://api.apiopen.top/videoCategory'
        #self.ep_path = 'mweather'
        self.cleint = HttpClient()

    @allure.story ('Test of shenzhen')
    def test_1(self):
        title = '#生活'
        itemid = '36'
        id = 0
        self._test(title,itemid,id)

    @allure.story('Test of shanghai')
    def test_2(self):
        title = '#动画'
        itemid = '10'
        id = 1
        self._test(title,itemid,id)

    @allure.story('Test of beijing')
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

