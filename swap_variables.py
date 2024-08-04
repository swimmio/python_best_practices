def swap_variables(x, y):
    """
    Prints `y: x` using a cool implementation
    >>> swap_variables(1, 2)
    2: 1
    >>> swap_variables('hello', 'world')
    world: hello
    """
    y, x = x, y
    # Don't change the line below - just add one line of code
    print(f'{x}: {y}')
