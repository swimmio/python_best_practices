# Add the type annotation
# Test that  `mypy --strict <filename>` passes!
# References:
# https://mypy.readthedocs.io/en/stable/builtin_types.html
# https://mypy.readthedocs.io/en/stable/type_inference_and_annotations.html
# This is new:
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html


def get_set_int(s) -> None:
    pass  # The implementation doesn't matter here


get_set_int({1, 2, 3, 4})
get_set_int(set([1, 2, 3, 4]))
