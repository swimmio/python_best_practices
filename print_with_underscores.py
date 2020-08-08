def print_with_underscores(my_list):
    """
    Using only `print`, this function prints all elements of `my_list`, with two underscores between elements.
    >>> print_with_underscores(["hello", "world", "from", "swimm"])
    hello__world__from__swimm
    """
    print(*my_list, sep='__')
