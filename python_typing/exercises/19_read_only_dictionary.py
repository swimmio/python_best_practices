# Add the type annotation
# Test that  `mypy --strict <filename>` passes!
# References:
# https://mypy.readthedocs.io/en/stable/builtin_types.html

# This is new:
# https://mypy.readthedocs.io/en/stable/more_types.html


def read_only_dictionary(d) -> None:
    pass  # The implementation doesn't matter here


read_only_dictionary(d={"a": 1})
