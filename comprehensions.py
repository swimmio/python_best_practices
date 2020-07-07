def squared_list(iterable):
    """
    Returns a list where every element of `iterable` is squared.
    Assumes all elements are ints.
    >>> squared_list([1,2,3])
    [1, 4, 9]
    """
    return [x ** 2 for x in iterable]


def squared_for_even_numbers(iterable):
    """
    Returns a list where every even element of `iterable` is squared.
    All odd elements of `iterable` are excluded from the returned list.
    Assumes all elements are ints.
    >>> squared_for_even_numbers([1,2,3,4])
    [4, 16]
    """
    return [x ** 2 for x in iterable if x % 2 == 0]


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


def reverse_dictionary(input_dict):
    """
    Returns a dictionary where every pair key: value in input_dict is reversed -
    that is, the value becomes the key and the key becomes the value.
    Assumes no duplications - every value in `input_dict` is unique.
    >>> reverse_dictionary({1: 'a', 2: 'b', 3: 'c'})
    {'a': 1, 'b': 2, 'c': 3}
    """
    return {v: k for k, v in input_dict.items()}
