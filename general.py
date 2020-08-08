def is_greater_than_2(number):
    """
    Returns True iff `number > 2`. Otherwise returns False.
    >>> is_greater_than_2(1)
    False
    >>> is_greater_than_2(2)
    False
    >>> is_greater_than_2(3)
    True
    >>> is_greater_than_2(100)
    True
    """
    # We don't need `if` or `else` here
    return number > 2


def print_with_underscores(my_list):
    """
    Using only `print`, this function prints all elements of `my_list`, with two underscores between elements.
    >>> print_with_underscores(["hello", "world", "from", "swimm"])
    hello__world__from__swimm
    """
    print(*my_list, sep='__')


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
