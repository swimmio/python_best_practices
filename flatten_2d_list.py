def flatten_2d_list(my_list):
    """
    Takes a list of two-members elements, and prints two flat tuples.
    >>> flatten_2d_list([['a', 'b'], ['c', 'd'], ['e', 'f']])
    ('a', 'c', 'e')
    ('b', 'd', 'f')
    """
    for element in zip(*my_list):
        print(element)
