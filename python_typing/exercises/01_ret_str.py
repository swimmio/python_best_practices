# ret_str is missing type annotation - so mypy is not happy.
# Add the right annotation.
# Test that  `mypy --strict <filename>` passes!
# References:
# https://mypy.readthedocs.io/en/stable/builtin_types.html

def ret_str():
    return "Swimm"
