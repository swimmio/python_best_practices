import math
from multiprocessing import Pool


def factorial(x):
    # Assume this function performs a heavy computation
    return math.factorial(x)


def multiple_factorial(iterable):
    """
    For every element in `iterable`, prints the factorial of this element on a separate line.
    Performs well.
    >>> multiple_factorial(range(10))
    1
    1
    2
    6
    24
    120
    720
    5040
    40320
    362880
    """
    with Pool(5) as p:
        for result in p.map(factorial, iterable):
            print(result)
