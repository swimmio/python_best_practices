# Add the type annotation
# Test that  `mypy --strict <filename>` passes!
# References:
# https://mypy.readthedocs.io/en/stable/builtin_types.html
# https://mypy.readthedocs.io/en/stable/type_inference_and_annotations.html
# https://mypy.readthedocs.io/en/stable/kinds_of_types.html

# This is new:
# https://mypy.readthedocs.io/en/stable/class_basics.html

class A:
    pass  # The implementation doesn't matter here


class B:
    def f(self, a):
        pass  # The implementation doesn't matter here


my_a = A()
my_b = B()
my_b.f(my_a)
