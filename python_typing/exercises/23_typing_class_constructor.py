# Add the type annotation
# Test that  `mypy --strict <filename>` passes!
# References:
# https://mypy.readthedocs.io/en/stable/builtin_types.html
# https://mypy.readthedocs.io/en/stable/type_inference_and_annotations.html
# https://mypy.readthedocs.io/en/stable/kinds_of_types.html

# This is new:
# https://mypy.readthedocs.io/en/stable/class_basics.html

class D:
    def __init__(self, c) -> None:
        pass  # The implementation doesn't matter here


class C:
    pass  # The implementation doesn't matter here


my_c = C()
my_d = D(my_c)
