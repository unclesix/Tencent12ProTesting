import pytest

def test_case1(login):              #（login）继承conftest.py中的公共方法def_login登陆方法，
    print("test_case1，需要登陆")
    pass
def test_case2():
    print("test_case2,不需要登陆")
    pass
def test_case3(login):
    print("test_case3，需要登陆")
    pass

if __name__ == '__main__':
    pytest.main()
