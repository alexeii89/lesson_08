class ComplexNumber:
    def __init__(self, z):
        self.a = int(z.real)
        self.b = int(z.imag)


    def __add__(self, other):
        return ComplexNumber(complex(other.a + self.a, (other.b + self.b)))

    def __mul__(self, other):
        return  ComplexNumber(complex(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a))

    def __str__(self):
        return f'{complex(self.a, self.b)}'


c_1 = ComplexNumber(9 - 12j)
c_2 = ComplexNumber(3 + 7j)


c_3 = c_1 + c_2
c_4 = c_1 * c_2
print(c_3)
print(c_4)