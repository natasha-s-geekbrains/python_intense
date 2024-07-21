"""На вход автоматически подаются две строки
frac1 и frac2 вида a/b - дробь с числителем и знаменателем.
Напишите программу, которая должна возвращать сумму и произведение дробей.
Дроби упрощать не нужно.
Для проверки своего кода используйте модуль fractions.
frac1 = "1/2"
frac2 = "1/3"
Сумма дробей: 5/6
Произведение дробей: 1/6

"""

import fractions

frac1 = "1/2"
frac2 = "1/3"

n1 = int(frac1[0])  # nominator (числитель дроби)
d1 = int(frac1[2])  # dedominator (знаменатель дроби)
n2 = int(frac2[0])
d2 = int(frac2[2])
print(f'n1 = {n1}')
print(f'd1 = {d1}')
print(f'n2 = {n2}')
print(f'd2 = {d2}')

gdc = 0  # Greatest common divisor (наибольший общий делитель)
denom1 = d1
denom2 = d2

while denom1 != 0 and denom2 != 0:
    if denom1 > denom2:
        denom1 = denom1 % denom2
    else:
        denom2 = denom2 % denom1
    gdc = denom1 + denom2
print(f'gdc = {gdc}')

lcm = int(d1 * d2 / gdc)  # Least common multiple (наименьшее общее кратное)
print(f'lcm = {lcm}')

n1_new = int(lcm / d1 * n1)
n2_new = int(lcm / d2 * n2)
n_res = n1_new + n2_new
print(f'n1_new = {n1_new}')
print(f'n2_new = {n2_new}')
print(f'n_res = {n_res}')

print(
    f'Сумма дробей: {n_res}/{lcm}\n'
    f'Произведение дробей: {n1 * n2}/{d1 * d2}\n'
    f'Сумма дробей: {n_res}/{lcm}\n'
    f'Произведение дробей: {n1 * n2}/{d1 * d2}\n'
)

print('\nCHECKING:')
f1 = fractions.Fraction(1, 2)
print(f'f1 = {f1}')
f2 = fractions.Fraction(1, 3)
print(f'f2 = {f2}')
print(f'Сумма дробей: {f1 + f2}')
print(f'Произведение дробей: {f1 * f2}')
print('\nCHECKING-2:')
fr1 = fractions.Fraction(frac1)
fr2 = fractions.Fraction(frac2)
print(f'fr1 = {fr1}')
print(f'fr1 = {fr2}')
print(f'Произведение дробей: {f1 * f2}')

