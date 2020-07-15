class D:
    def __init__(self, c: "C") -> None:
        pass  # The implementation doesn't matter here


class C:
    pass  # The implementation doesn't matter here


my_c = C()
my_d = D(my_c)
