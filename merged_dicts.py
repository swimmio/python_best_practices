def merge_dicts(dict_1, dict_2, dict_3):
    """
    Returns a dict that is a merge of the three input dicts.
    In case of duplicate keys, the last dictionary to have the key "wins".
    
    # Running the following line sould result in: {'a': 1, 'b': 3, 'c': 2, 'e': 3}
    >>> merged_dict = merge_dicts({'a': 1, 'b': 1}, {'b': 2, 'c': 2}, {'e': 3, 'b': 3})
    >>> sorted(merged_dict.items())
    [('a', 1), ('b', 3), ('c', 2), ('e', 3)]
    """
    return {**dict_1, **dict_2, **dict_3}
