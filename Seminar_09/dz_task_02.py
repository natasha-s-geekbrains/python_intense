code_to_write = '''
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
'''

with open("__init__.py", "w") as init_file:
    init_file.write(code_to_write)
