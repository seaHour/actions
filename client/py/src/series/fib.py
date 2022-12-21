import math


def fib(count):
    if count < 0:
        return math.nan
    elif count == 0 or count == 1:
        return count
    else:
        p0 = 0
        p1 = 1
        for _ in range(2, count+1):
            p2 = p0 + p1
            p0 = p1
            p1 = p2
        return p2
