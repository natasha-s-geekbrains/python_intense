"""
✔ Пользователь вводит строку текста.
✔ Подсчитайте сколько раз встречается
каждая буква в строке без использования
метода count и с ним.
✔ Результат сохраните в словаре, где ключ —
символ, а значение — частота встречи
символа в строке.
✔ Обратите внимание на порядок ключей.
Объясните почему они совпадают
или не совпадают в ваших решениях.
"""

my_text = input("Enter some text: \n")
my_dict = {}
new_my_text = my_text.replace(' ', '')

for letter in new_my_text:
    my_dict[letter] = my_dict.get(letter, 0) + 1
print(my_dict)

my_dict = {key: new_my_text.count(key) for key in set(new_my_text)}
print(my_dict)

# по вертикали
# for key, value in my_dict.items():
#     print(f'{key}: {value}')
# print(my_dict)
