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
    return all((s.isupper() for s in iterable))

# `all` is useful!