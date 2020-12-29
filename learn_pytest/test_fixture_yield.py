#yield  +  函数  == 生成器

# 例子：每次生成一个数据。直到for循环执行完
#python解释器执行。
# def provider():
#     for i in range(5):
#         print("before")
#         yield i       #生成器：类似于return i
#         print("after")
#
# p = provider()
# print(next(p))
# print(next(p))
# print(next(p))


import pytest

@pytest.fixture(scope="module")
def open():
    print("打开浏览器")
    yield
    print("执行teardown !")
    print("最后关闭浏览器")

def test_search1(open):
    print("test_search1")
    raise NameError
    pass

def test_search2(open):
    print("test_search2")
    pass

def test_search3(open):
    print("test_search3")
    pass

if __name__ == "__main__":
    pytest.main()