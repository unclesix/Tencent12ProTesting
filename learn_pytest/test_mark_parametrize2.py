import pytest
# pytest 参数化使用不同的类型

# 使用string类型
# a b c 对应方法中的变量，而元祖中的每个数字对应a b c的值
# @pytest.mark.parametrize("a,b,c",[(10,20,30),(10,30,5),(5,7,5)])
# def test_param(a,b,c):
#     print(a + b - c)

# 使用list
# @pytest.mark.parametrize(["a","b"],[(10,20),(2,30)])
# def test_param2(a,b):
#     print(a + b)

# 使用tuple
# @pytest.mark.parametrize(("a","b"),[(10,20),(2,30)])
# def test_parar3(a,b):
#     print(a + b)


# Yaml 实现参数化
import yaml


class Test_paramdemo():

    @pytest.mark.parametrize(("a", "b"), yaml.safe_load(open("D:\mylearntest\datas\data.yml")))
    def test_parar3(self,a, b):
        print(a - b)
