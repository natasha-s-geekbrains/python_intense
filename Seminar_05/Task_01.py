"""✔ Пользователь вводит строку из четырёх
или более целых чисел, разделённых символом “/”.
Сформируйте словарь, где:
✔второе и третье число являются ключами.
✔первое число является значением для первого ключа.
✔четвертое и все возможные последующие числа
 хранятся в кортеже как значения второго ключа.
"""

# if 1 == 1:
#     numbers = '10/12/1/4/28/30/35'
#     number_list = numbers.split('/')
#     key1, key2, key3 = int(number_list[0]), int(number_list[1]), int(number_list[2])
#     values = tuple(map(int, number_list[3:]))
#     my_dict = {key2: key1, key3: values}
#     print(my_dict)

# Variant 2


one, two, three, *other = input('Какой текст преобразовать? ').split('/')
print(map(int, other))
print(tuple(map(int, other)))
result = {
    int(two): int(one),
    int(three): tuple(map(int, other)),
}
print(f'{result=}')
