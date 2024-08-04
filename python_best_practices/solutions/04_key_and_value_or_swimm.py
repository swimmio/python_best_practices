def key_and_value_or_swimm(dictionary, key):
    """
    Receives a dictionary and a key.
    If the key exists within the dictionary - returns its corresponding value.
    Else, returns "swimm".
    >>> d = {"my_key": 1, "leet": 1337}
    >>> key_and_value_or_swimm(d, "my_key")
    1
    >>> key_and_value_or_swimm(d, "leet")
    1337
    >>> key_and_value_or_swimm(d, "non_existing")
    'swimm'
    """
    return dictionary.get(key, "swimm")
