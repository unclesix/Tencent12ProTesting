import pytest

#模块开始前执行
def setup_module():
    print("\n这是setup_module方法")

#整个模块结束后执行
def teardown_module():
    print("\n这是teardown_module方法")      #函数名与print要写对

#class外的方法执行前执行，
def setup_function():
    print("\nsetup_function")

#class外的方法执行后执行，
def teardown_function():
    print("\nteardown_function")

def test_login():
    print("\n这是一个外部的方法")

class Testdemo():
    #开始时执行setup_class
    def setup_class(self):
        print("\nsetup_class")

    def setup_method(self):
        print("\nsetup_method")

    def setup(self):
        print("\nsetup")

    #class 内所有方法执行完后执行teardown_class
    def teardown_class(self):
        print("\nteardown_class")           #函数名与print要写对

    def teardown_method(self):
        print("\nteardown_method")

    def teardown(self):
        print("\nteardown")

    def test_one(self):
        print("\n开始执行 test_one方法")
        x = 'this'
        assert 'h' in x
    def test_two(self):
        print("\n开始执行 test_two方法")
        x = 'hello'
        assert 'e' in x
    def test_three(self):
        print("\n开始执行 test_three方法")
        x = 'hello'
        x1 = 'hello world'
        assert x in x1

if __name__ == "__main__":
    #pytest.main()
    pytest.main("-v -s")       #方式2