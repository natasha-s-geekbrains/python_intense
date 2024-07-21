"""Вспоминаем задачу из семинара 8 про сериализацию данных,
где в бесконечном цикле запрашивали имя, личный
идентификатор и уровень доступа (от 1 до 7) сохраняя
информацию в JSON файл.
Напишите класс пользователя, который хранит эти данные в
свойствах экземпляра.
Отдельно напишите функцию, которая считывает информацию
из JSON файла и формирует множество пользователей.
file='users.json'
"""
import json


class User:
    def __init__(self, name: str, user_id: str, user_level: str):
        self.name = name
        self.user_id = user_id
        self.user_level = user_level

    def __str__(self):
        return f'[{self.name}, id={self.user_id}, level={self.user_level}]'

    def __repr__(self):
        return f'User({self.name}, {self.user_id}, {self.user_level})'


def load_json(filename):
    with open(filename, 'r', encoding='utf-8') as file_read:
        data = json.load(file_read)
    users_set = set()
    for level, users_dict in data.items():
        for user_id, name in users_dict.items():
            users_set.add(User(name=name, user_id=user_id, user_level=level))
    return users_set


if __name__ == '__main__':
    file = 'users.json'
    print(load_json(file))
    res = load_json(file)
    print(res)
    print(*res)
    for user in res:
        print(user)
    for user in res:
        print(user.name, user.user_id, user.user_level)
