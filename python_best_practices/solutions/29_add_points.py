import collections

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
