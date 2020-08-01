import collections


def counting_occurrences(iterable, element):
    """
    Use `collections` module to implement this function that returns how many times `element` appears in `iterable`.
    For example:
    >>> counting_occurrences(['swimm', 'hi', 'swimm', 'bye'], 'swimm')
    2
    >>> counting_occurrences(['swimm', 'hi', 'swimm', 'bye'], 'hi')
    1
    >>> counting_occurrences(['swimm', 'hi', 'swimm', 'bye'], 'non_existing')
    0
    """
    return collections.Counter(iterable)[element]
