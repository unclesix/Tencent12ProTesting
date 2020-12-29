import pytest
import requests

@pytest.fixture(params=[1,2,3])
def data(request):          #注意此处是定义一个固定参数来接收params的值。并不是requests模块包
    return request.param

def test_not_2(data):
    print(f"测试数据：{data}")
    assert data < 5
