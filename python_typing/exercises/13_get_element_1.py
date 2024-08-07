# Add the type annotation
# Test that  `mypy --strict <filename>` passes!
# References:
# https://mypy.readthedocs.io/en/stable/builtin_types.html
# https://mypy.readthedocs.io/en/stable/type_inference_and_annotations.html
# https://mypy.readthedocs.io/en/stable/kinds_of_types.html


def get_element_1(members):
    if len(members) < 2:
        return None
    return members[1]


get_element_1([1, 2, 3])
get_element_1((1, 2, 3))
