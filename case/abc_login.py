#1、根据规则 pytest.ini  python_files = 'abc_*.py' ，   Terminal中运行 ：pytest -vs   ;会搜索以abc开头的py文件
#2、python_classes = 'Login*'      运行Login实例
#3、python_functions = 'test_*'    运行test_开头的方法

class LoginCase:

    def test_login(self):
        print("login")

    def hogwards(self):
        print("hogwards")


class Test:
    def test_logout(self):
        print("logout")