def full_names(first_names, last_names):
    """
    Receives a list of first_names (e.g., ["Peter", "Tinker"]) and last_names (e.g., ["Pan", "Bell"])
    Prints full names by the corresponding indexes - one name per line. For example:
    >>> full_names(["Peter", "Tinker", "John", "Swimm"], ["Pan", "Bell", "Smith", "io"])
    Peter Pan
    Tinker Bell
    John Smith
    Swimm io
    """
    for (first_name, last_name) in zip(first_names, last_names):
        print(first_name, last_name)
