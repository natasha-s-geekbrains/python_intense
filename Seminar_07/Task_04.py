"""✔ Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
✔ расширение
✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
✔ минимальное число случайных байтов, записанных в файл, по умолчанию 256
✔ максимальное число случайных байтов, записанных в файл, по умолчанию 4096
✔ количество файлов, по умолчанию 3
✔ Имя файла и его размер должны быть в рамках переданного диапазона.
"""
from string import ascii_letters, ascii_lowercase
from random import randint, choices, randbytes


def file_gen(
        extent: str,
        min_len: int = 6,
        max_len: int = 30,
        min_size: int = 256,
        max_size: int = 4096,
        file_num: int = 3
) -> None:
    for _ in range(file_num):
        # data = bytes(randint(0,255)) for i in range(randint(min_size, max_size))
        data = randbytes(randint(min_size, max_size))
        file_name = ''.join(choices(ascii_lowercase + '_', k=randint(min_len, max_len)))
        with open(f'{file_name}.{extent}', 'wb') as f_wb:
            f_wb.write(data)


if __name__ == '__main__':
    file_gen('bin')
