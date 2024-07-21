"""Напишите программу, которая вычисляет площадь
круга и длину окружности по введённому диаметру.
✔ Диаметр не превышает 1000 у.е.
✔ Точность вычислений должна составлять
не менее 42 знаков после запятой.
"""

from math import pi
import decimal

decimal.getcontext().prec = 50
PI = decimal.Decimal(pi)

while (d := decimal.Decimal(input('Enter diameter: \n'))) > 1000:
    print('Enter a number less than 1000')

circle_length = PI * d
circle_square = PI * pow(d / 2, 2)
print(circle_length, circle_square)

circle_length = pi * float(d)
circle_square = pi * pow(float(d) / 2, 2)
print(circle_length, circle_square)
