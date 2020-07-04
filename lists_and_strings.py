def print_with_indexes(my_list):
    """
    Prints on every line: <index>: <value>
    For example:
    >>> print_with_indexes(['a', 'b', 'c'])
    0: a
    1: b
    2: c
    """
    # Using `enumerate` is very elegant in this case
    for (i, value) in enumerate(my_list):
        print('{}: {}'.format(i, value))


def last_element(my_list_or_string):
    """
    Returns the last element of a list or string
    >>> last_element([1,2,3])
    3
    >>> last_element(["hi", "swimm"])
    'swimm'
    >>> last_element("swimm")
    'm'
    """
    # This is very convenient in Python - there's no reason to use `len(my_list)`
    return my_list_or_string[-1]


def reverse(my_list_or_string):
    """
    Returns the list in reverse order
    >>> reverse([1,2,3])
    [3, 2, 1]
    >>> reverse("swimm")
    'mmiws'
    """
    # Here we use the slicing operator meaning we start from index 0, all the way to the end, with a
    # step of -1
    return my_list_or_string[::-1]

