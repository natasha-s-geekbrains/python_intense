"""Доработайте прошлую задачу добавив декоратор wraps в
каждый из декораторов."""

from typing import Callable
from random import randint
import os
import json
from functools import wraps


def number_control(func) -> Callable:
    min_attempts = 1
    max_attempts = 10
    min_guessing = 1
    max_guessing = 100

    @wraps(func)
    def wrapper(*args, **kwargs):
        guess, att = args
        guessing = guess if min_guessing <= guess <= max_guessing else randint(min_guessing, max_guessing)
        attempts = att if min_attempts <= att <= max_attempts else randint(min_attempts, max_attempts)
        return func(guessing, attempts)

    return wrapper


def deco_json(func):
    filename = f'{func.__name__}.json'
    if os.path.isfile(filename):
        with open(filename, 'r', encoding='utf-8') as f_r:
            data = json.load(f_r)
            print(data)
    else:
        data = []

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        json_dict = {'result': result, 'args': args, **kwargs}
        data.append(json_dict)
        with open(filename, 'w', encoding='utf-8') as f_w:
            json.dump(data, f_w, indent=4, ensure_ascii=False)

        return result

    return wrapper


def counter(num: int):
    def deco(func: Callable):
        my_list = []

        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num):
                my_list.append(func(*args, **kwargs))
            return my_list

        return wrapper

    return deco


@counter(3)
@number_control
@deco_json
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
    print(guessing_game.__name__)
    # guessing_game(10, 5)
