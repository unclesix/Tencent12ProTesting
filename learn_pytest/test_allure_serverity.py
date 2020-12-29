import allure
import pytest

def test_with_no_serverity_labl1():
    pass

@allure.severity(allure.severity_level.TRIVIAL)
def test_with_trival_serverity():
    pass
@allure.severity(allure.severity_level.NORMAL)
def test_with_normal_servrity():
    pass

@allure.severity(allure.severity_level.NORMAL)
class TestClassWithNormalServerity(object):
    def test_inside_the_normal_serverity_test_class(self):
        pass

    @allure.severity(allure.severity_level.CRITICAL)
    def test_inside_the_normal_serverity_test_class_with_critical_serverity(self):
        pass

if __name__== "__main__":
    pytest.main()