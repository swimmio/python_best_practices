def first_middle_last(iterable):
    """
    Receives an iterable and prints:
    - one line with its first element
    - a second line with a list of all elements but the first and last one
    - a third line with the last element
    >>> first_middle_last((1,2,3,4,5))
    1
    [2, 3, 4]
    5
    """
    first, *middle, last = iterable
    print(first)
    print(middle)
    print(last)

# "Tuple unpacking is cool! Read more about it:
# https://www.geeksforgeeks.org/unpacking-a-tuple-in-python/