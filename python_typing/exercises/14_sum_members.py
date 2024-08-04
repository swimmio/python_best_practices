# Add the type annotation
# Test that  `mypy --strict <filename>` passes!
# References:
# https://mypy.readthedocs.io/en/stable/builtin_types.html
# https://mypy.readthedocs.io/en/stable/type_inference_and_annotations.html
# https://mypy.readthedocs.io/en/stable/kinds_of_types.html


def sum_members(members):
    sm = 0
    for mem in members:
        sm += mem
    return sm


sum_members([1, 2, 3])
sum_members((1, 2, 3))
sum_members({1, 2, 3})
sum_members({1: 1, 2: 2, 3: 3})
sum_members(range(1, 4))
