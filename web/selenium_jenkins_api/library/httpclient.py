
import requests
import urllib3

class HttpClient:

    #disable_ssl_verify=Flase 关闭https接口类型认证
    def __init__(self,disable_ssl_verify = False ,timeout= 60):
        self.client = requests.session()
        self.disable_ssl_verify = disable_ssl_verify
        self.timeout = timeout
        #如果位https类型验证，则发出警告异常
        if self.disable_ssl_verify:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def Get(self, url, headers=None, data=None,json=None, params=None,*args,**kwargs):
        """Http get method"""

        if headers is None:
            headers = {}

        if self.disable_ssl_verify:
            response = self.client.get(url, headers=headers, data=data, json = json, params = params
                                       , verify = False, timeout = self.timeout , *args, **kwargs)
        else:
            response = self.client.get(url, headers = headers, data= data, json = json, params = params
                                       , timeout = self.timeout , *args, **kwargs)

        response.encoding = 'utf_8_sig'
        print(f'{response.json()}')

        return  response