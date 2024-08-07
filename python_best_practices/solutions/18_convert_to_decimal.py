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
