import pytest

#autouser = Ture 将open方法适用于所有的用例，且用例中不需要再继承open方法
@pytest.fixture(autouse=True)
def open():
    print("打开浏览器")


#用例中不需要继承open方法
def test_search1():
    print("test_search1")
    raise NameError
    pass

def test_search2():
    print("test_search2")
    pass

def test_search3():
    print("test_search3")
    pass

if __name__ == "__main__":
    pytest.main()