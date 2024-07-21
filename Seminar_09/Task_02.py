"""Дорабатываем задачу 1.
Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные в функциюугадайку
числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами
из диапазонов."""

from typing import Callable
from random import randint


def number_control(func) -> Callable:
    min_attempts = 1
    max_attempts = 10
    min_guessing = 1
    max_guessing = 100

    def wrapper(*args, **kwargs):
        guess, att = args
        guessing = guess if min_guessing <= guess <= max_guessing else randint(min_guessing, max_guessing)
        attempts = att if min_attempts <= att <= max_attempts else randint(min_attempts, max_attempts)
        return func(guessing, attempts)

    return wrapper


@number_control
def guessing_game(guessing: int, attempts: int):
    for i in range(attempts):
        print(f'Попытка #{i + 1}')
        var = int(input('Угадай число: '))
        if var == guessing:
            print('Вы угадали, браво!!')
            return
    print('Количество попыток исчерпано')
    return


if __name__ == '__main__':
    guessing_game(10, 5)
