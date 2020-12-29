import pytest

def test_a():
    print("执行test_a")
class Test_demo():
    def test_one(self):
        print("开始执行 test_one方法")
        x = 'this'
        #assert 'h' in x
        pytest.assume('h' not in  x)        #assume 方法中存在多条断言，都会执行，并打印错误的断言信息
        pytest.assume( 1 == 2)
        pytest.assume(x in 'this is')
    def test_two(self):
        print("开始执行 test_two方法")
        x = 'hello'
        assert 'e' in x

    def test_three(self):
        print("开始执行 test_three方法")
        x = 'hello'
        x1 = 'hello world'
        assert x not in x1

class Test_demo1():
    def test_a(self):
        print("开始执行 test_a方法")
        x = 'this'
        assert 'h' in x

    def test_b(self):
        print("开始执行 test_b方法")
        x = 'hello'
        assert 'e' in x

    def test_c(self):
        print("开始执行 test_c方法")
        x = 'hello'
        x1 = 'hello world'
        assert x in x1


if __name__ == "__main__":
    pytest.main()                        #默认方式，也会打印
    #pytest.main("-v -x Test_demo")           #方式1
    #pytest.main(['-v','-s','Test_demo'])       #方式2