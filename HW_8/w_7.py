class Complex:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b
        self.k = complex(self.a, self.b)

    def __add__(self, other):
        y = self.k + other.k
        return Complex(y.real, y.imag)

    def __mul__(self, other):
        x = self.k * other.k
        return Complex(x.real, x.imag)

    def __str__(self):
        return f'{self.k}'


c = Complex(1, 2)
d = Complex(3, 4)
print(c + d)
print(c * d)
