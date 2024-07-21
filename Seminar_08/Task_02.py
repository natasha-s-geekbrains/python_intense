"""Напишите функцию, которая в бесконечном цикле
запрашивает имя, личный идентификатор и уровень
доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в
JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключом для имени.
Убедитесь, что все идентификаторы уникальны независимо
от уровня доступа.
При перезапуске функции уже записанные в файл данные
должны сохраняться."""

import json
from pathlib import Path


def set_user(path: Path) -> None:
    id_set = set()
    if path.is_file():
        with open(path, 'r', encoding='utf-8') as f:
            data_dict = json.load(f)
            for id_name in data_dict.values():
                id_set.update(id_name)
    else:
        data_dict = {str(level): {} for level in range(1, 7 + 1)}

    while True:
        name = input('Enter your name:\n')
        if not name:
            break
        id = input('Enter your id:\n')
        if id not in id_set:
            id_set.update(id)
            level = input('Enter your access level:\n')
            # data_dict[level].update({id: name})
            data_dict[level][id] = name
        else:
            print(f'Entered id is not unique')

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data_dict, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    set_user(Path('users.json'))
