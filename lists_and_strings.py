def swap_variables(x, y):
    """
    Prints `y: x` using a cool implementation
    >>> swap_variables(1, 2)
    2: 1
    >>> swap_variables('hello', 'world')
    world: hello
    """
    y, x = x, y
    # Don't change the line below - just add one line of code
    print('{}: {}'.format(x, y))


def filter_string_starting_with_a(list_of_strings):
    """
    Returns a list of all the strings in `_list_of_strings` starting with `a`:
    >>> filter_string_starting_with_a(["hello", "abc", "Abraham", "all my loving"])
    ['abc', 'all my loving']
    """
    return list(filter(lambda x: x.startswith('a'), list_of_strings))
    # Alternatively:
    # return [s for s in list_of_strings if s.startswith('a')]


def filter_none_and_friends(my_list):
    """
    Returns a list that contains all elements within `my_list`, but not  False, None, empty string/dict/set/list and `0`
    >>> filter_none_and_friends(["hello", '', {}, {'a':1}, [], [1], 0, 1, None, False, True])
    ['hello', {'a': 1}, [1], 1, True]
    """
    return list(filter(None, my_list))


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
