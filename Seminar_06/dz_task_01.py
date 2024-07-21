"""Вы работаете над разработкой программы для проверки корректности даты, введенной пользователем.
На вход будет подаваться дата в формате "день.месяц.год".
Ваша задача - создать программу, которая проверяет, является ли введенная дата корректной или нет.
Ваша программа должна предоставить ответ "True" (дата корректна) или "False" (дата некорректна)
в зависимости от результата проверки.
date_to_prove = 15.4.2023
date_to_prove = 31.6.2022
date_to_prove = '0.5.2022'
date_to_prove = '12.0.2022'
date_to_prove = '12.5.-2022'
date_to_prove = '29.2.2020'
"""


def _is_leap_year(in_year):
    if (in_year % 4 == 0 and in_year % 100 != 0) or in_year % 400 == 0:
        return True
    else:
        return False


def check_date(str_date):
    day, month, year = str_date.split('.')
    if not (day.isdigit() and month.isdigit() and year.isdigit()):
        return False

    day, month, year = map(int, str_date.split('.'))
    if 1 <= year <= 9999:
        if month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31:
            return True
        elif month in [4, 6, 9, 11] and 1 <= day <= 30:
            return True
        elif month == 2 and 1 <= day <= 28 + _is_leap_year(year):
            return True
    return False


date_to_prove = '31.6.2022'
if __name__ == '__main__':
    print(check_date(date_to_prove))






