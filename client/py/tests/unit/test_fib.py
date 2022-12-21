import pytest
import math
import series.fib


def fib(count):
    if count == 0 or count == 1:
        return count
    else:
        return fib(count-1) + fib(count-2)


@pytest.mark.parametrize("index", [1, 5, 7, 8, 11, 16])
def test_fib_base(index):
    assert fib(index) == series.fib.fib(index)


@pytest.mark.parametrize("index", [-1, -5, -7, -16])
def test_fib_negative(index):
    assert series.fib.fib(index) is math.nan
