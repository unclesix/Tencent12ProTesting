import pytest

from util.Calc import Calc
import yaml
def getdata(datapath,datakey):
    testdata = yaml.safe_load(open(datapath))
    return testdata[datakey]

class Test_calc:
    def setup(self):
        self.calc = Calc()
    @pytest.mark.parametrize("a,b,c",getdata('../data/data.yaml','add'))
    def calc_add(self, a, b, c):
        try:
            rest = self.calc.add(a, b)
        except TypeError:
            assert b == None or a == None
        else:
            assert c == rest

    @pytest.mark.parametrize("a,b,c",getdata('../data/data.yaml','div'))
    def calc_div(self, a, b, c):
        try:
            rest = self.calc.div(a, b)
        except ZeroDivisionError:
            assert b == 0
        except TypeError:
            assert b == None or a == None
        else:
            assert c == rest

    @pytest.mark.parametrize("a,b,c",getdata('../data/data.yaml','sub'))
    def calc_sub(self, a, b, c):
        rest = self.calc.sub(a, b)
        assert c == rest

    @pytest.mark.parametrize("a,b,c",getdata('../data/data.yaml','mul'))
    def calc_mul(self, a, b, c):
        rest = self.calc.mul(a, b)
        assert c == rest


if __name__ == '__main__':
    pytest.main()
