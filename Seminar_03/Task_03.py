"""
Создайте вручную кортеж содержащий элементы разных типов.
✔ Получите из него словарь списков, где:
ключ — тип элемента,
значение — список элементов данного типа.
"""

data = (42, 73, 3.14, 'Hello world!', None, True, 'Text', 100500.2, False)

my_dict = {}

for item in data:
    if type(item).__name__ not in my_dict:
        my_dict[type(item).__name__] = [item]
    else:
        my_dict[type(item).__name__].append(item)
print(my_dict)

print('VARIANT-2')

my_dict = {}

for item in data:
    my_dict[type(item).__name__] = my_dict.get(type(item).__name__, [])
    my_dict[type(item).__name__].append(item)
print(my_dict)

print('VARIANT-3')

my_dict = {}

for item in data:
    my_dict.setdefault(type(item).__name__, []).append(item)
print(my_dict)


print('VARIANT-4')

# my_dict = {}

my_dict = {type(item): [] for item in data}
[my_dict[type(item)].append(item) for item in data]

print(my_dict)





