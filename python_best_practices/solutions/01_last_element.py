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
    return my_list_or_string[-1]


# Using my_list[-1] is very convenient in Python - there's no reason to use `len(my_list)` in this case.