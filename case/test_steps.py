import pytest
import yaml

from util.Calc import Calc


# 读取steps数据文件，拥有一个列表，add 与 add1
def opensteps():
    with open("../datas/steps.yaml") as f:
        return yaml.safe_load(f)

class Test_Calc2:
    def setup(self):
        self.calc = Calc()

    @pytest.mark.parametrize('data1,data2,expect', yaml.safe_load(open('../datas/add.yaml')))
    def test_calc_add(self,data1,data2,expect):
        s = opensteps()
        for step in s:     #不要再次引用s() ，否则汇报”TypeError: 'list' object is not callable“
            print(f"step ====> {step}")
            if 'add' == step:
                result = self.calc.add(data1,data2)
            elif 'add1' == step:
                result = self.calc.add1(data1,data2)
            assert expect == result


if __name__ == '__main__':
    pytest.main()

