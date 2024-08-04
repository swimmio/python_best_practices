def reverse(my_list_or_string):
    """
    Returns the list in reverse order
    >>> reverse([1,2,3])
    [3, 2, 1]
    >>> reverse("swimm")
    'mmiws'
    """
    return my_list_or_string[::-1]

# Here we use the slicing operator meaning we start from index `0`, all the way to the end, with a `step` of `-1`