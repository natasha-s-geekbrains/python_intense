"""Прочитайте созданный в прошлом задании csv файл без
использования csv.DictReader.
Распечатайте его как pickle строку.
"""

import csv
import pickle
from pathlib import Path


def csv_2_pickles(path: Path) -> None:
    pickle_list = []
    with open(path, 'r', encoding='utf-8', newline='') as f_read:
        csv_file = csv.reader(f_read)
        for i, line in enumerate(csv_file):
            if i == 0:
                headers = line
            else:
                pickle_dict = {key: value for key, value in zip(headers, line)}
                # print(*zip(headers, line))
                pickle_list.append(pickle_list)

    print(pickle.dumps(pickle_list))


if __name__ == '__main__':
    csv_2_pickles(Path('new_users.csv'))
