from math import *


def f(x):
    return x ** 2 + 3 * x + 1


def zero(f, a, b):
    if f(a) * f(b) > 0:
        print("la fontion ne s'annulle pas dans l'interval ["+str(a)+", "+str(b)+"]")
        return 0
    while abs(a - b) > (e - 3):
        m = (a + b) / 2
        print(m)
        if f(m) * f(a) > 0:
            a = m
        else:
            b = m
        print('la solution de f(x) = 0 est'+str(m))
        return m
