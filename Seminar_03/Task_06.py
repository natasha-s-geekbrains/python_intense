"""
Пользователь вводит строку текста. Вывести каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого длинного
слова был один пробел между ним и номером строки.
"""

value = input("Введите несколько слов: \n").split()
value.sort()

max_len = max(len(item) for item in value)
for i, item in enumerate(value, 1):
    print(f'{i} {item: >{max_len}}')

max_len2 = 0
for item in value:
    if len(item) > max_len2:
        max_len2 = len(item)

for i, item in enumerate(value, 1):
    print(f'{i} {item: >{max_len2}}')
