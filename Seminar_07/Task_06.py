"""✔ Дорабатываем функции из предыдущих задач.
✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
(добавьте проверки).
✔ Существующие файлы не должны удаляться/изменяться
в случае совпадения имён."""
import os
from string import digits, ascii_lowercase
from random import randint, choices, randbytes
from pathlib import Path


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
        with open(f'{Path.cwd()}\\{file_name}.{extent}', 'wb') as f_wb:
            f_wb.write(data)


def gen_files(path: str | Path, **kwargs) -> None:
    if isinstance(path, str):
        path = Path(path)
    if not path.is_dir():
        path.mkdir(parents=True)
    os.chdir(path)
    for extent, count in kwargs.items():
        file_gen(extent, file_num=count)


if __name__ == '__main__':
    gen_files(r'C:\Users\iru\PycharmProjects\pythonProject1\Seminar_07\ex1\test', txt=2, jpeg=1)
