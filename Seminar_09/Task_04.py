"""Создайте декоратор с параметром.
Параметр - целое число, количество запусков декорируемой
функции."""

from typing import Callable


def counter(num: int):
    def deco(func: Callable):
        my_list = []

        def wrapper(*args, **kwargs):
            for _ in range(num):
                my_list.append(func(*args, **kwargs))
            return my_list

        return wrapper

    return deco


@counter(3)
def upper_text(text: str):
    return text.upper()


if __name__ == '__main__':
    print(upper_text('Спать хочу!!!!'))
