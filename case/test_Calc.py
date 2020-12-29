"""
编写 Calc 这个类的所有的方法的测试用例
按照等价类去设计测试用例并实现
把代码上传到github, 并回贴你的github的地址
"""

import pytest

from util.Calc import Calc

import yaml
def getdata(datapath,datakey):
    testdata = yaml.safe_load(open(datapath))
    return testdata[datakey]


class Test_calc:
    def setup(self):
        self.calc = Calc()

    #不要忘记pytest 用例函数要以“test_”开头    ！！！
    @pytest.mark.parametrize("data1,data2,expect",getdata('../datas/data.yaml','add'))
    def test_calc_add(self, data1, data2, expect):
        try:
            rest = self.calc.add(data1, data2)
        except TypeError:
            assert data1 == None or data2 == None
        else:
            assert expect == rest

    @pytest.mark.parametrize("data1,data2,expect",getdata('../datas/data.yaml','div'))
    def test_calc_div(self, data1, data2, expect):
        try:
            rest = self.calc.div(data1, data2)
        except ZeroDivisionError:
            assert data2 == 0
        except TypeError:
            assert data2 == None or data1 == None
        else:
            assert expect == rest

    @pytest.mark.parametrize("data1,data2,expect",getdata('../datas/data.yaml','sub'))
    def test_calc_sub(self, data1, data2, expect):
        rest = self.calc.sub(data1, data2)
        assert expect == rest

    @pytest.mark.parametrize("data1,data2,expect",getdata('../datas/data.yaml','mul'))
    def test_calc_mul(self, data1, data2, expect):
        rest = self.calc.mul(data1, data2)
        assert expect == rest


if __name__ == '__main__':
    pytest.main()
