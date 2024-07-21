"""
1.

Создайте функцию generate_csv_file(file_name, rows),
которая будет генерировать по три случайны числа в каждой строке,
от 100-1000 строк, и записывать их в CSV-файл. Функция принимает два аргумента:
- file_name (строка) - имя файла, в который будут записаны данные.
- rows(целое число) - количество строк (записей) данных, которые нужно сгенерировать.

generate_csv_file("input_data.csv", 101)

2.

Создайте функцию find_roots(a, b, c),
которая будет находить корни квадратного уравнения вида ax^2 + bx + c = 0.
Функция принимает три аргумента:
a, b, c (целые числа) - коэффициенты квадратного уравнения.

Функция возвращает:
- None, если уравнение не имеет корней (дискриминант отрицателен).
- Одно число, если уравнение имеет один корень (дискриминант равен нулю).
- Два числа (корни), если уравнение имеет два корня (дискриминант положителен).

find_roots("input_data.csv")

3.

Создайте декоратор save_to_json(func), который будет оборачивать функцию find_roots.
Декоратор выполняет следующие действия:
 - Читает данные из CSV-файла, переданного в аргументе функции, исходя из аргумента args[0].
 - Для каждой строки данных вычисляет корни квадратного уравнения с помощью функции find_roots.
 - Сохраняет результаты в формате JSON в файл results.json.
 Каждая запись JSON содержит параметры a, b, c и результаты вычислений.


ИТОГ:
Таким образом, после выполнения функций generate_csv_file и find_roots
в файле results.json будет сохранена информация
о параметрах и результатах вычислений для каждой строки данных из CSV-файла.

with open("results.json", 'r') as f:
    data = json.load(f)

if 100<=len(data)<=1000:
    print(True)
else:
    print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")

print(len(data)==101)

На выходе:
True
True

Формат JSON файла определён следующим образом:

[
    {"parameters": [a, b, c], "result": result},
    {"parameters": [a, b, c], "result": result},
    ...
]

"""

import csv
from random import randint
import json


def generate_csv_file(file_name: str, rows: int) -> None:
    """Функция генерирует по три случайны числа в каждой строке,
и записывает их в CSV-файл"""

    var_num = 3
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        for _ in range(rows):
            nums_str = [randint(1, 10) for _ in range(var_num)]
            writer.writerow(nums_str)


def save_to_json(func):
    """Это декоратор, который читает данные из CSV-файла
    и сохраняет результат работы декорируемой функции в формате JSON в файл"""

    def wrapper(*args, **kwargs):

        source_file = args[0]
        json_dict = []
        with open(source_file, 'r') as file_read:
            csv_file = csv.reader(file_read)
            for row in csv_file:
                a, b, c = map(int, row)
                result = func(a, b, c)
                json_dict.append({'parameters': [a, b, c], 'result': result})

        with open('results.json', 'w', encoding='utf-8') as file_write:
            json.dump(json_dict, file_write, indent=2, ensure_ascii=False)

    return wrapper


@save_to_json
def find_roots(a: int, b: int, c: int):
    """Эта функция принимает коэффициенты квадратного уравнения из csv-файла
    и возвращает результат решения этого уравнения"""

    d = b ** 2 - 4 * a * c

    if d < 0:
        result = None

    elif d == 0:
        x = -b / (2 * a)
        result = x

    else:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        x_list = [x1, x2]

        result = x_list
    return result


if __name__ == '__main__':
    generate_csv_file("input_data.csv", 101)
    find_roots('input_data.csv')

    with open("results.json", 'r') as f:
        data = json.load(f)

    if 100 <= len(data) <= 1000:
        print(True)
    else:
        print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")

    print(len(data) == 101)
