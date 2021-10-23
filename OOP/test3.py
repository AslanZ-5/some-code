from test import FirstClass


class ThirdClass(FirstClass):  # Inherit from SecondClass
    def __init__(self, value):  # On "ThirdClass(value)"
        self.data = value

    def __add__(self, other):  # On "self + other"
        return ThirdClass(self.data + other)

    def __str__(self):  # On "print(self)", "str()"

        return '[ThirdClass: %s]' % self.data

    def mul(self, other):  # In-place change: named
        self.data *= other

x = ThirdClass('aslan')
b = ThirdClass('zurabov')
# print(x.data + 'musa')

# print(a)
print(ThirdClass.__bases__)