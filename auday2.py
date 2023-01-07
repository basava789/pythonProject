import pytest
def func(x):
    return x +6
def test_func():
    assert func(4)==10

@pytest.mark.parametrize("num,result", [(1, 11), (2, 22), (3, 33), (4, 44), (5, 55)])
def test_calu(num, result):
    assert 11*num == result
