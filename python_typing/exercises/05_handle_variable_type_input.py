# Fix the type annotation
# Test that  `mypy --strict <filename>` passes!
# References:
# https://mypy.readthedocs.io/en/stable/builtin_types.html
# https://mypy.readthedocs.io/en/stable/type_inference_and_annotations.html

def handle_variable_type_input(str_int) -> int:
    """
    This function returns 5 if the input is of type string
    otherwise it returns the value.

    Note - str_int can be either of type `int` or `str`.
    """
    if isinstance(str_int, str):
        return 5
    else:
        return str_int
