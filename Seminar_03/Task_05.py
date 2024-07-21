"""
✔ Создайте вручную список с повторяющимися целыми числами.
✔ Сформируйте список с порядковыми номерами
нечётных элементов исходного списка.
✔ Нумерация начинается с единицы.
"""

data = [42, 73, 5, 42, 42, 2, 3, 5, 7, 73, 42]
new_data = []

for i, item in enumerate(data, 1):
    if item % 2 != 0:
        new_data.append(i)

print(new_data)

print('VARIANT-2')

new_data = [i for i, item in enumerate(data, 1) if item % 2 != 0]

print(new_data)
