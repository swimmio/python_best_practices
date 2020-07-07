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


def sort_by_third_element(iterable):
    """
    This function gets a list of tuples and returns the list sorted by its third element.
    For example:
    >>> sort_by_third_element([(1,2,3), (1,5,9), (1,1,1)])
    [(1, 1, 1), (1, 2, 3), (1, 5, 9)]
    >>> sort_by_third_element([(1,2,3,4), (1,5,9,1023), (1,1,1)])
    [(1, 1, 1), (1, 2, 3, 4), (1, 5, 9, 1023)]
    """
    import operator
    return sorted(iterable, key=operator.itemgetter(2))


def is_only_upper_strings(iterable):
    """
    Returns True iff every string within `iterable` contains only uppercase characters.
    >>> is_only_upper_strings(["SWIMM", "UNIT", "SWIMMING"])
    True
    >>> is_only_upper_strings(["SWImm", "UNIT", "SWIMMING"])
    False
    >>> is_only_upper_strings(["SWIMM", "UNIT", "SWimmING"])
    False
    """
    return all([s.isupper() for s in iterable])


def is_any_string_upper_here(iterable):
    """
    Returns True iff there is at least one string within `iterable` that contains only uppercase characters.
    >>> is_any_string_upper_here(["SWIMM", "UNIT", "SWIMMING"])
    True
    >>> is_any_string_upper_here(["SWIMM", "UNit", "swimming"])
    True
    >>> is_any_string_upper_here(["swimm", "UNIt", "swIMMING"])
    False
    """
    return any([s.isupper() for s in iterable])


def full_names(first_names, last_names):
    """
    Receives a list of first_names (e.g., ["Peter", "Tinker"]) and last_names (e.g., ["Pan", "Bell"])
    Prints full names by the corresponding indexes - one name per line. For example:
    >>> full_names(["Peter", "Tinker", "John", "Swimm"], ["Pan", "Bell", "Smith", "io"])
    Peter Pan
    Tinker Bell
    John Smith
    Swimm io
    """
    for (first_name, last_name) in zip(first_names, last_names):
        print(first_name, last_name)


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
