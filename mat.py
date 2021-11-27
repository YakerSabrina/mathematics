class Complex:
    def __init__(self, real, imag):
        self.a = real
        self.b = imag

    def add(self, another_complex_numb):
        return Complex(self.a + another_complex_numb.a, self.b + another_complex_numb.b)

    def sub(self, another_complex_numb):
        return Complex(self.a - another_complex_numb.a, self.b - another_complex_numb.b)

    def multi(self, another_complex_numb):
        return Complex((self.a * another_complex_numb.a) - (self.b * another_complex_numb.b),
                       (self.b * another_complex_numb.a) + (self.a * another_complex_numb.b))


def suite_fibonnachi(n):
    a = 0
    b = 1
    suite = [a]
    while b < n:
        a, b = b, a + b
        suite.append(a)
    print(suite)
