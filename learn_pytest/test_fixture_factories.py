#1.make_customer_record 中再写一个方法，定义返回一个变量name
#2.在测试用例中可多次调用make_customer_record，并动态传入name值。
import pytest

@pytest.fixture
def make_customer_record():
    def _make_customer_record(name):
        return {"name": name, "orders": []}

    return _make_customer_record


def test_customer_records(make_customer_record):
    customer_1 = make_customer_record("Lisa")
    customer_2 = make_customer_record("Mike")
    customer_3 = make_customer_record("Meredith")