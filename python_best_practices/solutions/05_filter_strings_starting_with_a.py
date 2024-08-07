def filter_string_starting_with_a(list_of_strings):
    """
    Returns a list of all the strings in `_list_of_strings` starting with `a`:
    >>> filter_string_starting_with_a(["hello", "abc", "Abraham", "all my loving"])
    ['abc', 'all my loving']
    """
    return list(filter(lambda x: x.startswith('a'), list_of_strings))
    # Alternatively:
    # return [s for s in list_of_strings if s.startswith('a')]
