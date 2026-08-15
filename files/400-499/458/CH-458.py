import math


# First spy numbers over 1000.
def is_spy(number):
    digs = list(map(int, str(number)))
    return sum(digs) == math.prod(digs)


result = list(filter(is_spy, range(1000, 10001)))[:7]
