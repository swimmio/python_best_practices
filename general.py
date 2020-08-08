def convert_to_decimal(input_number, base):
    """
    Returns the decimal representation of `input_number` given in base `base`.
    >>> convert_to_decimal(101, 2)
    5
    >>> convert_to_decimal(101, 8)
    65
    >>> convert_to_decimal(101, 16)
    257
    """
    return int(str(input_number), base)


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
