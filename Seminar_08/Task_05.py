"""Напишите функцию, которая ищет json файлы в указанной
директории и сохраняет их содержимое в виде
одноимённых pickle файлов."""

import pickle
from pathlib import Path
import json


def json_2_pickle(path: Path) -> None:
    for file in path.iterdir():
        if file.suffix == '.json':
            with (
                open(file, 'r', encoding='utf-8') as f_read,
                open(f'{file.stem}.pickle', 'wb') as f_write
            ):
                res = json.load(f_read)
                pickle.dump(res, f_write)


if __name__ == '__main__':
    json_2_pickle(Path(r'C:\Users\iru\PycharmProjects\pythonProject1\Seminar_08'))
