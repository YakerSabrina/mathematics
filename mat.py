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


def suite_fibonacci(n):
    a = 0
    b = 1
    suite = [a]
    if n == 0:
        print("0! = 1")
    else:
        while b < n:
            a, b = b, a + b
            suite.append(a)
        print(suite)


def factorial(n):
    k = 1
    i = 1
    if k == 0:
        print("0! = 1")
    else:
        while i <= n:
            k = k * i
            i += 1
        print(k)


def signe(n):
    listep = []
    listen = []
    dico = {"positif" : listep,
            "negatif" : listen}
    if n >= 0:
        listep.append(n)
    else:
        listen.append(n)
    print(dico)
