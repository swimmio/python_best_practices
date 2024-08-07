def squared_set(iterable):
    """
    Returns a list where every element of `iterable` is squared.
    Since this is a set, having `2` and `-2` in `iterable` will result in one instance of `4` only.
    Assumes all elements are ints.
    >>> squared_set([1,2,3,-3,4,3])
    {16, 1, 4, 9}
    """
    # set comprehensions are cool!
    return {x ** 2 for x in iterable}

# https://python-reference.readthedocs.io/en/latest/docs/comprehensions/set_comprehension.html