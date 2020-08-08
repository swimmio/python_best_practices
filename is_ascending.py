def is_ascending(a, b, c):
    """
    a, b, c are ascending if a<b and also b<c.
    For example:
    >>> is_ascending(1,5,20)
    True
    >>> is_ascending(7,5,20)
    False
    >>> is_ascending(1,1,20)
    False
    >>> is_ascending(200,100,20)
    False
    >>> is_ascending(-1,5,20)
    True
    """
    return a < b < c
