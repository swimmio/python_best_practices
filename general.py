def numbers_dict():
    """
    >>> numbers_dict()
    {'one': 1, 'thousand': 1000, 'million': 1000000}
    """
    # Using numeric literals (with `_`) improve readability
    return {'one': 1, 'thousand': 1_000, 'million': 1_000_000}


def pretty_print_number(number):
    """
    Returns a string representation of `number` where every three digits (from the right) are delimited by `,`
    >>> pretty_print_number(10)
    '10'
    >>> pretty_print_number(10000)
    '10,000'
    >>> pretty_print_number(2**32)
    '4,294,967,296'
    """
    return format(number, ',')
