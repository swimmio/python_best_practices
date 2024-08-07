def reverse_dictionary(input_dict):
    """
    Returns a dictionary where every pair key: value in input_dict is reversed -
    that is, the value becomes the key and the key becomes the value.
    Assumes no duplications - every value in `input_dict` is unique.
    >>> reverse_dictionary({1: 'a', 2: 'b', 3: 'c'})
    {'a': 1, 'b': 2, 'c': 3}
    """
    return {v: k for k, v in input_dict.items()}

# [dict comprehensions](https://python-reference.readthedocs.io/en/latest/docs/comprehensions/dict_comprehension.html) are awesome