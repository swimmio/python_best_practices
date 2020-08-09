def squared_list(iterable):
    """
    Returns a list where every element of `iterable` is squared.
    Assumes all elements are ints.
    >>> squared_list([1,2,3])
    [1, 4, 9]
    """
    return [x ** 2 for x in iterable]
