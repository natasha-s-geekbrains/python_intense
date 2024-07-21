"""✔ Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции.
"""

import random
from pathlib import Path


def random_editor(str_num: int, file_name: str | Path) -> None:
    with open(file_name, 'a', encoding='utf-8') as file:
        for _ in range(str_num):
            int_num = random.randint(-1000, 1000)
            float_num = random.uniform(-1000, 1000)
            file.write(f'{int_num} | {float_num}\n')
            # print(f'{int_num} | {float_num}', file=file)


if __name__ == '__main__':
    random_editor(33, 'numbers.txt')
