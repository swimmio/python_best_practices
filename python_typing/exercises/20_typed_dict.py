# Add the type annotation
# Test that  `mypy --strict <filename>` passes!
# References:
# https://mypy.readthedocs.io/en/stable/builtin_types.html

# This is new:
# https://mypy.readthedocs.io/en/stable/more_types.html


def ret_typed_dict():
    return {
        "str_field": "str",
        "int_field": 0,
        "float_field": 0.0,
        "list_field": [1, 2, 3],
        "optional_str_field": None
    }


_: MySpecialDict = ret_typed_dict()
