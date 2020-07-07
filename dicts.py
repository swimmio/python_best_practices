import collections


def key_and_value_or_swimm(dictionary, key):
    """
    Receives a dictionary and a key.
    If the key exists within the dictionary - returns its corresponding value.
    Else, returns "swimm".
    >>> d = {"my_key": 1, "leet": 1337}
    >>> key_and_value_or_swimm(d, "my_key")
    1
    >>> key_and_value_or_swimm(d, "leet")
    1337
    >>> key_and_value_or_swimm(d, "non_existing")
    'swimm'
    """
    # Note: `get` has a second argument of a default value. This is a very elegant solution.
    return dictionary.get(key, "swimm")


def sum_of_keys(input_dict):
    """
    Receives `input_dict`, and returns a dictionary where every key is the a value in `input_dict`,
    and the value is the sum of corresponding keys.
    >>> output = sum_of_keys({1: "hello", 2: "swimm", 4: "hello", 10: "swimm", 5: "io"})
    >>> output['hello']
    5
    >>> output['swimm']
    12
    >>> output['io']
    5
    """
    return_dict = collections.defaultdict(int)
    for key, value in input_dict.items():
        return_dict[value] += key

    return return_dict


def merge_dicts(dict_1, dict_2, dict_3):
    """
    Returns a dict that is a merge of the three input dicts.
    In case of duplicate keys, the last dictionary to have the key "wins".
    >>> merge_dicts({'a': 1, 'b': 1}, {'b': 2, 'c': 2}, {'e': 3, 'b': 3})
    {'a': 1, 'b': 3, 'c': 2, 'e': 3}
    """
    return {**dict_1, **dict_2, **dict_3}
