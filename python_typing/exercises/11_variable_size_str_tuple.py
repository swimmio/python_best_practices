# Add the type annotation
# Test that  `mypy --strict <filename>` passes!
# References:
# https://mypy.readthedocs.io/en/stable/builtin_types.html
# https://mypy.readthedocs.io/en/stable/type_inference_and_annotations.html
# https://mypy.readthedocs.io/en/stable/kinds_of_types.html


def variable_size_str_tuple(tup):
    return ",".join(tup)


variable_size_str_tuple(tuple())
variable_size_str_tuple(("a", "b"))
