class A:
    pass  # The implementation doesn't matter here


class B:
    def f(self, a: A) -> None:
        pass  # The implementation doesn't matter here


my_a = A()
my_b = B()
my_b.f(my_a)
