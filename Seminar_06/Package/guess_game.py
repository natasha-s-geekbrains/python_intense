"""Задание №2
� Создайте модуль с функцией внутри.
� Функция принимает на вход три целых числа: нижнюю и
верхнюю границу и количество попыток.
� Внутри генерируется случайное число в указанных границах
и пользователь должен угадать его за заданное число
попыток.
� Функция выводит подсказки “больше” и “меньше”.
� Если число угадано, возвращается истина, а если попытки
исчерпаны - ложь."""

import random
from sys import argv

__all__ = ['guess_number']


def guess_number(lower_limit: int, upper_limit: int, attempts: int) -> bool:
    hidden_number = random.randint(lower_limit, upper_limit)
    for item in range(1, attempts + 1):
        print(f'Attempt number: {item}')
        user_number = int(input('Enter a number of your choice: '))
        if user_number < hidden_number:
            print('Your number is less than target')
        elif user_number > hidden_number:
            print('Your number is greater than target')
        else:
            print('You are right!')
            return True
    print('Your attempts are over!')
    return False


if __name__ == '__main__':
    # print(argv)
    # guess_number(int(argv[1]), int(argv[2]), int(argv[3]))
    # guess_number(*(int(num) for num in argv[1:]))
    name, *param = argv
    print(param)
    guess_number(*(int(num) for num in param))


# (venv) PS C:\Users\iru\PycharmProjects\pythonProject1\Seminar_06>
# python guess_game.py 3 7 3