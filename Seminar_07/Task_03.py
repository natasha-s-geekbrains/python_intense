"""✔ Напишите функцию, которая открывает на чтение созданные
в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните
имя и произведение:
✔ если результат умножения отрицательный, сохраните имя
записанное строчными буквами и произведение по модулю
✔ если результат умножения положительный, сохраните имя
прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк,
сколько в более длинном файле.
✔ При достижении конца более короткого файла,
возвращайтесь в его начало"""

from pathlib import Path
from typing import TextIO


def read_line_or_begin(fd: TextIO) -> str:
    line = fd.readline()
    if line == '':
        fd.seek(0)
        line = fd.readline()
    return line[:-1]


def convert(names: str | Path, numbers: str | Path, results: str | Path) -> None:
    with(
        open(names, 'r', encoding='utf-8') as f_names,
        open(numbers, 'r', encoding='utf-8') as f_numbers,
        open(results, 'w', encoding='utf-8') as f_results
    ):
        # len_names = len(f_names.readlines())
        # len_numbers = len(f_numbers.readlines())
        print(f_names)
        len_names = sum(1 for _ in f_names)
        len_numbers = sum(1 for _ in f_numbers)
        for _ in range(max(len_names, len_numbers)):
            name = read_line_or_begin(f_names)
            print(name)
            number = read_line_or_begin(f_numbers)
            a, b = map(float, number.split(' | '))
            res = a * b
            if res < 0:
                f_results.write(f'{name.lower()} {-res}\n')
            elif res > 0:
                f_results.write(f'{name.upper()} {round(res)}\n')


if __name__ == '__main__':
    convert(Path('names.txt'), Path('numbers.txt'), Path('results.txt'))
