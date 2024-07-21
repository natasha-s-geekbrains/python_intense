"""
Вы работаете над разработкой программы для проверки корректности даты, введенной пользователем.
На вход будет подаваться дата в формате "день.месяц.год".
Ваша задача - создать программу, которая проверяет, является ли введенная дата корректной или нет.
Ваша программа должна предоставить ответ "True" (дата корректна) или "False" (дата некорректна)
в зависимости от результата проверки.
Добавьте логирование ошибок и полезной
информации. Также реализуйте возможность запуска из
командной строки с передачей параметров.
"""

import logging
import os
import argparse

current_file = os.path.realpath(__file__)
path = f'\'{current_file}\''
log_file_name = os.path.splitext(os.path.basename(path))[0]

FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
         'в строке {lineno:03d} функция "{funcName}()" ' \
         'в {created} секунд записала сообщение: {msg}'

logging.basicConfig(format=FORMAT, style='{', level=logging.NOTSET, filemode='w', filename='dz_sem15_file.log',
                    encoding='utf-8')
logger = logging.getLogger(f'{log_file_name}')


def _is_leap_year(in_year):
    if (in_year % 4 == 0 and in_year % 100 != 0) or in_year % 400 == 0:
        logger.info(f'Год {in_year} является високосным')
        return True
    else:
        logger.info(f'Год {in_year} не является високосным')
        return False


def check_date(str_date):
    logger.info(f'Получен строковой аргумент "{str_date}"')
    try:
        day, month, year = str_date.split('.')
        if not (day.isdigit() and month.isdigit() and year.isdigit()):
            logger.error('Неверный формат даты')
    except ValueError:
        logger.error('Неверный формат: невозможно перевести данные в дату')
        return False

    day, month, year = map(int, str_date.split('.'))
    logger.info(f'Строковая дата переведена в числа {day} {month} {year}')
    year_range = range(1, 9999 + 1)
    if year not in year_range:
        logger.error(f'Значение года {year} находится вне заданного диапазона {year_range}.')
        return False
    day_month_message = f'Проверка окончена: {day}.{month}.{year} является корректной датой'
    if month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31:
        logger.info(day_month_message)
        return True
    elif month in [4, 6, 9, 11] and 1 <= day <= 30:
        logger.info(day_month_message)
        return True
    elif month == 2 and 1 <= day <= 28 + _is_leap_year(year):
        logger.info(day_month_message)
        return True
    logger.warning(f'Проверка окончена: {day}.{month}.{year} не является корректной датой')
    return False


def parse_str_date():
    parser = argparse.ArgumentParser(
        description='Проверяет полученную строковую дату на корректность, логирует информацию.',
        prog='check_date()',
        epilog='Возвращает истину или ложь. Логирует информацию в файл dz_sem15_file.log.'
    )
    parser.add_argument('str_date', metavar='string_date', type=str,
                        help='Введите дату в формате "день.месяц.год". Например: 25.4.1998')
    args = parser.parse_args()
    return check_date(args.str_date)


if __name__ == '__main__':
    print(parse_str_date())
