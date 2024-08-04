def sort_by_third_element(iterable):
    """
    This function gets a list of tuples and returns the list sorted by its third element.
    For example:
    >>> sort_by_third_element([(1,2,3), (1,5,9), (1,1,1)])
    [(1, 1, 1), (1, 2, 3), (1, 5, 9)]
    >>> sort_by_third_element([(1,2,3,4), (1,5,9,1023), (1,1,1)])
    [(1, 1, 1), (1, 2, 3, 4), (1, 5, 9, 1023)]
    """
    import operator
    return sorted(iterable, key=operator.itemgetter(2))
