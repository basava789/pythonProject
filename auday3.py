import pytest
import allure
def add(a,b):
    return a+b
def fact(n):
    if n<0:
        return -1
    elif n==1:
        return 1
    else:
        f=1
        for i in range(1,n+1):
            f=f*i
        return f

def test_add1():
     assert add(10, 12) == 22
@pytest.mark.add
def test_add2():
    assert add(10, 4) == 14
@pytest.mark.add
def test_add3():
    assert add(-10, 20) == 10
def test_fact():
    assert fact(-4) == -1
    assert fact(0) == 1
    assert fact(5) == 120
    assert fact(1) == 1
