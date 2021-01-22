def numbers_dict():
    """
    >>> numbers = numbers_dict()
    >>> numbers['one']
    1
    >>> numbers['thousand']
    1000
    >>> numbers['million']
    1000000
    >>> 1_000 == 1_0_0_0 == 1000 == 100_0
    True
    """
    return {'one': 1, 'thousand': 1_000, 'million': 1_000_000}
