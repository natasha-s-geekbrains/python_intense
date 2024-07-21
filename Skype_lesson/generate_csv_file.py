import csv
from random import randint


def generate_csv_file(file_name: str, rows: int) -> str:
    """Функция генерирует по три случайны числа в каждой строке,
и записывает их в CSV-файл"""

    var_num = 3
    with open(file_name, 'w', newline='') as file:
        for _ in range(rows):
            nums_str = ' '.join(str(randint(1, 10)) for _ in range(var_num))
            writer = csv.writer(file)
            writer.writerow([nums_str])
    return file_name


if __name__ == '__main__':
    generate_csv_file("input_data.csv", 5)