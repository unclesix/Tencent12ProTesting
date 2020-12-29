
# 1.conftest.py文件名字是固定的，不可以做任何修改
# 2.文件和用例文件在同一个目录下，那么conftest.py作用于整个目录
# 3.conftest.py文件所在目录必须存在__init__.py文件
# 4.conftest.py文件不能被其他文件导入，不需要import导入conftest.py，pytest用例会自动查找
# 5.所有同目录测试文件运行前都会执行conftest.py文件
# 6.全局的配置和前期工作都可以卸载这里，放在某个包下，就是这个包数据共享的地方
import pytest

@pytest.fixture()
def login():
    print("这是个登陆方法")

def pytest_configure(config):
    marker_list = ['search','login']
    for markers in marker_list:
        config.addinivalue_line("markers",markers
                                )


a = "hello"
assert 'e' in a