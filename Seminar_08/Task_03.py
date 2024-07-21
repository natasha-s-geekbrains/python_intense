"""Напишите функцию, которая сохраняет созданный в
прошлом задании файл в формате CSV.
"""
import csv
import json
from pathlib import Path


def json_2_csv(path: Path) -> None:
    with (
        open(path, 'r', encoding='utf-8') as f_read,
        open(path.stem + '.csv', 'w', encoding='utf-8', newline='') as f_write
    ):
        data = json.load(f_read)
        rows_list = []
        for level, id_name in data.items():
            for id, name in id_name.items():
                rows_list.append({'level':level,  'id': id, 'name': name})

        csv_write = csv.DictWriter(
            f_write,
            fieldnames=['level', 'id', 'name', 'other'],
            dialect='excel',
            restval='Hello world',
            quoting=csv.QUOTE_NONNUMERIC
        )
        csv_write.writeheader()
        csv_write.writerows(rows_list)


if __name__ == '__main__':
    json_2_csv(Path('users.json'))
