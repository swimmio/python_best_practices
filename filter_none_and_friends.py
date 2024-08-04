def filter_none_and_friends(my_list):
    """
    Returns a list that contains all elements within `my_list`, but not  False, None, empty string/dict/set/list and `0`
    >>> filter_none_and_friends(["hello", '', {}, {'a':1}, [], [1], 0, 1, None, False, True])
    ['hello', {'a': 1}, [1], 1, True]
    """
    return list(filter(None, my_list))
