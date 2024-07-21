"""✔ Напишите функцию, которая генерирует
псевдоимена.
✔ Имя должно начинаться с заглавной буквы,
состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
✔ Полученные имена сохраните в файл."""

from random import randint, choice
from pathlib import Path

VOWELS = 'eyuioa'
CONSONANTS = 'qwrtpsdfghjklzxcvbnm'
MIN_LEN = 4
MAX_LEN = 7


def pseudonames_gen(str_num: int, file_name: str | Path) -> None:
    with open(file_name, 'a', encoding='utf-8') as f:
        flag: bool = choice([True, False])
        for _ in range(str_num):
            name = ''
            for i in range(randint(MIN_LEN, MAX_LEN)):
                if flag:
                    name += choice(VOWELS)
                else:
                    name += choice(CONSONANTS)
                flag = not flag
            f.write(name.title() + '\n')


if __name__ == '__main__':
    pseudonames_gen(10, 'names.txt')
