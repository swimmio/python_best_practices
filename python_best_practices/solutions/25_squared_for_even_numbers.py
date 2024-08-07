def squared_for_even_numbers(iterable):
    """
    Returns a list where every even element of `iterable` is squared.
    All odd elements of `iterable` are excluded from the returned list.
    Assumes all elements are ints.
    >>> squared_for_even_numbers([1,2,3,4])
    [4, 16]
    """
    return [x ** 2 for x in iterable if x % 2 == 0]

# Comprehensions also support if/else - as you can see here:
# https://stackoverflow.com/questions/4260280/if-else-in-a-list-comprehension