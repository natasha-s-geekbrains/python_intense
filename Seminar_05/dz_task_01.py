"""Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
На входе:
file_path = "C:/Users/User/Documents/example.txt"
file_path = '/home/user/data/file.py'
file_path = 'D:/myfile.txt'
file_path = 'C:/Projects/project1/code/script.py'
file_path = '/home/user/docs/my.file.with.dots.txt'
file_path = 'file_in_current_directory.txt'
На выходе:
('C:/Users/User/Documents/', 'example', '.txt')
"""

import os.path


def my_get_file_info(*, file_path) -> tuple:
    path, file_name = os.path.split(file_path)
    if path == '':
        final_path = path
    else:
        final_path = path + '/'
    name, ext = os.path.splitext(file_name)
    return final_path, name, ext

# РЕШЕНИЕ GB


def get_file_info(file_path):
    file_name = file_path.split("/")[-1]
    file_extension = file_name.split(".")[-1]
    path = file_path[:-len(file_name)]
    return path, file_name[:-len(file_extension)-1], "." + file_extension


print(my_get_file_info(
    file_path='file_in_current_directory.txt'))

print(get_file_info(
    file_path='file_in_current_directory.txt'))
