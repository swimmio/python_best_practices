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
    return any((s.isupper() for s in iterable))

# `any` is useful!