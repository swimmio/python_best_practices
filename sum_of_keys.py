import collections


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
