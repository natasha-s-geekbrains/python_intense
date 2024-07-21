import csv
import json


def save_to_json(func):
    """Это декоратор, который читает данные из CSV-файла
    и сохраняет результат работы декорируемой функции в формате JSON в файл"""

    source_file = "input_data.csv"
    line_num = 1
    with open(source_file, 'r', encoding='utf-8', newline='') as file_read:
        csv_file = csv.reader(file_read)
        all_file_list = [row for row in csv_file]
        one_str_list = all_file_list[line_num][0].split()
        res_list = []
        for i in one_str_list:
            res_list.append(int(i))

    def wrapper(*args, **kwargs):
        """Эта функция сохраняет результат работы декорируемой функции в формате JSON в файл"""

        result = func(*args, **kwargs)
        json_dict = {'parameters': res_list, 'result': result}
        with open('results.json', 'w', encoding='utf-8') as file_write:
            json.dump(json_dict, file_write, indent=2, ensure_ascii=False)

        return result

    return wrapper


@save_to_json
def find_roots(from_file: str, index_num: int):
    """Эта функция принимает коэффициенты квадратного уравнения из csv-файла
    и возвращает результат решения этого уравнения"""

    with open(from_file, 'r', encoding='utf-8', newline='') as file_read:
        csv_file = csv.reader(file_read)
        all_file_list = [row for row in csv_file]
        one_str_list = all_file_list[index_num][0].split()
        res_list = []
        for i in one_str_list:
            res_list.append(int(i))
        a, b, c = res_list

        d = b ** 2 - 4 * a * c
        print(f'{d=}')

        result = ''
        if d < 0:
            result = None

        elif d == 0:
            x = -b / 2 / a
            result = x

        else:
            x1 = (-b + d ** 0.5) / (2 * a)
            x2 = (-b - d ** 0.5) / (2 * a)
            x_list = [x1, x2]

            result = x_list
    return result


if __name__ == '__main__':
    find_roots('input_data.csv', 1)
