import pytest

def func(x):
    return x + 1

def test_answer():          #识别test_  或者尾部 _test
    assert func(3) == 5