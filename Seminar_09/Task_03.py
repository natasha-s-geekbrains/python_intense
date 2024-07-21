"""Напишите декоратор.
Декоратор должен сохранять в json файл
параметры декорируемой функции и
результат, который она возвращает.
При повторном вызове файл должен расширяться, а не перезаписываться.
Каждый ключевой параметр сохраните как отдельный ключ json словаря.
Для декорирования напишите функцию, которая может
принимать как позиционные, так и ключевые аргументы.
Имя файла должно совпадать с именем декорируемой
функции."""

import json
import os


def deco_json(func):
    filename = f'{func.__name__}.json'
    if os.path.isfile(filename):
        with open(filename, 'r', encoding='utf-8') as f_r:
            data = json.load(f_r)
            print(data)
    else:
        data = []

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        json_dict = {'result': result, 'args': args, **kwargs}
        data.append(json_dict)
        with open(filename, 'w', encoding='utf-8') as f_w:
            json.dump(data, f_w, indent=4, ensure_ascii=False)

        return result

    return wrapper


@deco_json
def sum_numbers(*args, **kwargs):
    return sum(args)


def mult_numbers(*args, **kwargs):
    return args[0] * args[1]


mult_numbers = deco_json(mult_numbers)
mult_numbers(100, 999)

if __name__ == '__main__':
    sum_numbers(10, 5, 15, 16, z=8, c='Привет')
    sum_numbers(x=20, y=3)
    sum_numbers(100, 999)

