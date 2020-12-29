import pytest

# #参数化，前两个变量，后面是对应的数据；
# # 3+5 ->test_input   8->expected\
# @pytest.mark.parametrize("test_input,expected",[("3+5",8),("2+5",7),("7*5",30)])
# def test_eval(test_input,expected):
#     # eval 将字符串str 当成有效表达式来求值，并返回，比如3+5=8
#     assert eval(test_input) == expected



#参数组合

# @pytest.mark.parametrize("x",[1,2])
# @pytest.mark.parametrize("y",[8,10,11])
# def test_foo(x,y):
#     print("\n测试数据组合 x:{},y:{}".format(x,y))

# 方法名作为参数
import sys
test_user_date = ["Tom","Jerry"]
@pytest.fixture(scope="module")
def login_r(request):
    # 这是接收并传入的参数，继承request方法，通过request.param方法接收
    user = request.param
    print("\n 打开首页准备登陆，登陆用户：{}".format(user))
    return user     #将user名字返回打印

# indirect = True  ,可以把传过来的参数当函数来执行，意思是说会先调用login_r方法，test_user_date被当做参数传入到login_r方法中。
# 可以实现一个方法，形成两个测试用例的。
@pytest.mark.parametrize("login_r",test_user_date,indirect = True)
#@pytest.mark.skip("此次测试版本未上线，不执行")
#@pytest.mark.skipif(sys.platform == "darwin",reason ='不在macos上执行')
#@pytest.mark.xfail      #只是标注一下，通过，即使是错误的
def test_login(login_r):
    a = login_r
    print("\n 测试用例中login的返回值：{}".format(a))
    assert a != ""

if __name__ == "__main__":
    pytest.main("-v -s")