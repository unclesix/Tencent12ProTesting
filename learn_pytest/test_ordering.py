import pytest

class TestPytest(object):
    @pytest.mark.run(order=-1)
    def test_two(self):
        print("test_two,ceshiyongli")

    @pytest.mark.run(order=1)
    def test_one(self):
        print("test_one ceshiyongli")

    @pytest.mark.run(order=3)
    def test_three(self):
        print("test_three ceshiyongli")