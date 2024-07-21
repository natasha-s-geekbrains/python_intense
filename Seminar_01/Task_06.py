"""Напишите программу, которая запрашивает год и проверяет его на високосность.
Распишите все возможные проверки в цепочке elif.
Откажитесь от магических чисел
Обязательно учтите год ввода Григорианского календаря
В коде должны быть один input и один print"""


REFORM = 1582
BIG_LEAP_YEAR = 400
LARGE_NOW_LEAP_YEAR = 100
SMALL_LEAP_YEAR = 4
MULTIPLE = 0

year = int(input('Enter year: '))

if year < REFORM:
    result = 'Year not Grigorian'
elif year % BIG_LEAP_YEAR == MULTIPLE:
    result = f'{year} is a leap year'
elif year % LARGE_NOW_LEAP_YEAR == MULTIPLE:
    result = f'{year} is not a leap year'
elif year % SMALL_LEAP_YEAR == MULTIPLE:
    result = f'{year} is a leap year'
else:
    result = f'{year} is not a leap year'

print(result)

