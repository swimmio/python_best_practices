def squared_generator(iterable):
    """
    Returns a generator that yields elements of `iterable`, with their value - squared.
    Assumes all elements are ints.
    >>> g = squared_generator([1,2,3])
    >>> type(g)
    <class 'generator'>
    >>> list(g)
    [1, 4, 9]
    """
    return (x ** 2 for x in iterable)
