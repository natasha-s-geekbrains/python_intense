"""Задание №7.
Создайте модуль и напишите в нём функцию, которая
получает на вход дату в формате DD.MM.YYYY
� Функция возвращает истину, если дата может существовать
или ложь, если такая дата невозможна.
� Для простоты договоримся, что год может быть в диапазоне
[1, 9999].
� Весь период (1 января 1 года - 31 декабря 9999 года)
действует Григорианский календарь.
� Проверку года на високосность вынести в отдельную
защищённую функцию."""

__all__ = ['is_valid_date']


def _is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


def is_valid_date(date: str) -> bool:
    day, month, year = map(int, date.split('.'))
    if 1 <= year <= 9999:
        if month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31:
            return True
        elif month in [4, 6, 9, 11] and 1 <= day <= 30:
            return True
        elif month == 2 and 1 <= day <= 28 + _is_leap_year(year):
            return True
    return False


if __name__ == '__main__':
    print(is_valid_date('02.12.2000'))
    print(is_valid_date('02.12.1001'))
    print(is_valid_date('02.23.2000'))
    print(is_valid_date('50.12.2000'))
    print(is_valid_date('02.12.10000'))
    print(is_valid_date('29.02.2024'))
