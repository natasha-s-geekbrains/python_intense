"""Из созданных на уроке и в рамках домашнего задания функций,
соберите пакет для работы с файлами.

Создайте файл __init__.py и запишите в него функцию rename_files"""

import os


def create_init_file():
    file_name = '__init__.py'
    with open(file_name, 'w') as file:
        pass
    with open(file_name, 'r+') as file:
        file.write("[def rename_files]\n")
        file.seek(0)
        print(file.read())


if __name__ == '__main__':
    create_init_file()

    with open("__init__.py", "r") as init_file:
        code = init_file.read()

    function_names = [
        "def rename_files"
    ]

    for func_name in function_names:
        if func_name not in code:
            print(f"Функция {func_name} не найдена в файле __init__.py")
        else:
            print(f"Функция {func_name} найдена в файле __init__.py")
