from mat import *
if __name__ == '__main__':
    number1 = Complex(1, 4)
    number2 = Complex(2, 3)
    num_add = number1.add(number2)
    num_sous = number1.sub(number2)
    num_multi = number1.multi(number2)

    print('({} + {}i) + ({} + {}i) = {} + {}i'.format(number1.a, number1.b, number2.a, number2.b, num_add.a, num_add.b))
    print('({} + {}i) - ({} + {}i) = {} - {}i'.format(number1.a, number1.b, number2.a, number2.b, num_sous.a, num_sous.b))
    print('({} + {}i) + ({} + {}i) = {} + {}i'.format(number1.a, number1.b, number2.a, number2.b, num_multi.a, num_multi.b))