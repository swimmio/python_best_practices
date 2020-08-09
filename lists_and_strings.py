def flatten_2d_list(my_list):
    """
    Takes a list of two-members elements, and prints two flat lists.
    >>> flatten_2d_list([['a', 'b'], ['c', 'd'], ['e', 'f']])
    ('a', 'c', 'e')
    ('b', 'd', 'f')
    """
    for element in zip(*my_list):
        print(element)


def path_join(*args):
    """
    Receives paths and joins them by '/'
    >>> path_join('a', 'b', 'c')
    'a/b/c'
    """
    return '/'.join(args)


def first_middle_last(iterable):
    """
    Receives an iterable and prints:
    - one line with its first element
    - a second line with a list of all elements but the first and last one
    - a third line with the last element
    >>> first_middle_last((1,2,3,4,5))
    1
    [2, 3, 4]
    5
    """
    first, *middle, last = iterable
    print(first)
    print(middle)
    print(last)
