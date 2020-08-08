def default_value(argument):
    """
    Returns `argument` in case it's not None or False. Otherwise returns `swimm`.
    For example:
    >>> default_value("hello")
    'hello'
    >>> default_value(23)
    23
    >>> default_value(None)
    'swimm'
    """
    return argument or 'swimm'
