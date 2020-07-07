import collections
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


def counting_occurrences(iterable, element):
    """
    Use `collections` module to implement this function that returns how many times `element` appears in `iterable`.
    For example:
    >>> counting_occurrences(['swimm', 'hi', 'swimm', 'bye'], 'swimm')
    2
    >>> counting_occurrences(['swimm', 'hi', 'swimm', 'bye'], 'hi')
    1
    >>> counting_occurrences(['swimm', 'hi', 'swimm', 'bye'], 'non_existing')
    0
    """
    return collections.Counter(iterable)[element]


Point = collections.namedtuple('Point', ['x', 'y'])


def add_points(p1, p2):
    """
    >>> p1 = Point(x=0, y=0)
    >>> p2 = Point(1, 2)
    >>> p3 = add_points(p1, p2)
    >>> p3
    Point(x=1, y=2)
    >>> p3[0] == p3.x
    True
    >>> p3 == p2
    True
    """
    return Point(p1.x + p2.x, p1.y + p2.y)
