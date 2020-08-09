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
