"""Ваша задача - написать программу, которая принимает на вход директорию
и рекурсивно обходит эту директорию и все вложенные директории.

Результаты обхода должны быть сохранены в нескольких форматах: JSON, CSV и Pickle.

Каждый результат должен содержать следующую информацию:
- Путь к файлу или директории: Абсолютный путь к файлу или директории.
- Тип объекта: Это файл или директория.
- Размер: Для файлов - размер в байтах, для директорий - размер, учитывая все вложенные файлы и директории в байтах.
- Важные детали:
    * Для дочерних объектов (как файлов, так и директорий) укажите родительскую директорию.
    * Для файлов сохраните их размер в байтах.
    * Для директорий,
        помимо их размера,
        учтите размер всех файлов и директорий, находящихся внутри данной директории, и вложенных директорий.

Программа должна использовать рекурсивный обход директорий, чтобы учесть все вложенные объекты.
Результаты должны быть сохранены в трех форматах: JSON, CSV и Pickle. Форматы файлов должны быть выбираемыми.
Для обхода файловой системы вы можете использовать модуль os.

Вам необходимо написать функцию traverse_directory(directory), которая будет выполнять обход директории
и возвращать результаты в виде списка словарей.
После этого результаты должны быть сохранены в трех различных файлах (JSON, CSV и Pickle)
с помощью функций save_results_to_json, save_results_to_csv и save_results_to_pickle.

Файлы добавляются в список results в том порядке, в котором они встречаются при рекурсивном обходе директорий.
При этом сначала добавляются файлы, а затем директории.

Для каждого файла (name в files), сначала создается полный путь к файлу (path = os.path.join(root, name)),
и затем получается размер файла (size = os.path.getsize(path)).
Информация о файле добавляется в список results в виде словаря {'Path': path, 'Type': 'File', 'Size': size}.

Затем, для каждой директории (name в dirs), также создается полный путь к директории (path = os.path.join(root, name)),
 и вызывается функция get_dir_size(path), чтобы получить размер всей директории с учетом ее содержимого.
 Информация о директории добавляется в список results в виде словаря
 {'Path': path, 'Type': 'Directory', 'Size': size}."""

import os
import json
import csv
import pickle


def old_get_dir_size(start_path='.'):
    dir_size = 0
    for root, dir_names, file_names in os.walk(start_path):
        for file_name in file_names:
            file_path = os.path.join(root, file_name)
            dir_size += os.path.getsize(file_path)
        for dir_name in dir_names:
            dir_path = os.path.join(root, dir_name)
            # dir_size += get_dir_size(dir_path)
            dir_size += os.path.getsize(dir_path)
    return dir_size


def get_dir_size(directory):
    total_size = 0
    for root, dirs, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            total_size += os.path.getsize(path)
    return total_size


def save_results_to_json(res_list: [], file_name):
    with open(file_name, 'w',) as file:
        json.dump(res_list, file, indent=4)

#
# def save_results_to_csv(res_list: [], file_name):
#     with open(file_name, 'w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(['Path', 'Type', 'Size'])
#         for result in res_list:
#             writer.writerow([result['Path'], result['Type'], result['Size']])


def save_results_to_csv(results, file_path):
    with open(file_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Path', 'Type', 'Size'])
        writer.writeheader()
        writer.writerows(results)


def save_results_to_pickle(res_list: [], file_name):
    with open(file_name, 'wb') as file:
        pickle.dump(res_list, file)


def traverse_directory(directory):
    results = []
    for root, dirs, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            size = os.path.getsize(path)
            results.append({'Path': path, 'Type': 'File', 'Size': size})
        for name in dirs:
            path = str(os.path.join(root, name))
            size = get_dir_size(path)
            results.append({'Path': path, 'Type': 'Directory', 'Size': size})
    return results


def read_directory(dict_list: list) -> None:
    for dict_ in dict_list[:]:
        print(dict_)


read_directory(traverse_directory(r'C:\Users\iru\PycharmProjects\pythonProject1\Seminar_08'))
result_list = traverse_directory(r'C:\Users\iru\PycharmProjects\pythonProject1\Seminar_08')

save_results_to_json(result_list, file_name='res_json')
save_results_to_csv(result_list, 'res_csv.csv')
save_results_to_pickle(result_list, 'res_pickle.pkl')
