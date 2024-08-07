def print_with_indexes(my_list):
    """
    Prints on every line: <index>: <value>
    For example:
    >>> print_with_indexes(['a', 'b', 'c'])
    0: a
    1: b
    2: c
    """
    for (i, value) in enumerate(my_list):
        print(f'{i}: {value}')

# Using `enumerate` is very elegant in this case!