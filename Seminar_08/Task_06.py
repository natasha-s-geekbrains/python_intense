"""Напишите функцию, которая преобразует pickle файл
хранящий список словарей в табличный csv файл.
Для тестирования возьмите pickle версию файла из задачи
4 этого семинара.
Функция должна извлекать ключи словаря для заголовков
столбца из переданного файла.
"""

import pickle
import csv
from pathlib import Path


def pickle_2_csv(path: Path) -> None:
    with(
        open(path, 'rb') as f_read,
        open(f'{path.stem}.csv', 'w', encoding='utf-8', newline='') as f_write
    ):
        pickle_var = pickle.load(f_read)
        headers = list(pickle_var[0])
        csv_write = csv.DictWriter(
            f_write,
            fieldnames=headers,
            dialect='excel',
            quoting=csv.QUOTE_NONNUMERIC
        )

        csv_write.writeheader()
        csv_write.writerows(pickle_var)


if __name__ == '__main__':
    pickle_2_csv(Path('new_users.pickle'))
