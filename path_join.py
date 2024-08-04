def path_join(*args):
    """
    Receives paths and joins them by '/'
    >>> path_join('a', 'b', 'c')
    'a/b/c'
    """
    return '/'.join(args)
