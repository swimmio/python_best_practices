# Add the type annotation
# Test that  `mypy --strict <filename>` passes!
# References:
# https://mypy.readthedocs.io/en/stable/builtin_types.html
# https://mypy.readthedocs.io/en/stable/type_inference_and_annotations.html
# https://mypy.readthedocs.io/en/stable/kinds_of_types.html

def add_int_str(a, b):
    return a + b


assert add_int_str(1, 1) == 2
assert add_int_str("Swimm ", "is awesome") == "Swimm is awesome"
