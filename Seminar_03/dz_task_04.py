"""Дан список повторяющихся элементов lst. Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
lst = [1, 1, 2, 2, 3, 3]
[1, 2, 3]"""

lst = [1, 2, 2, 3, 3, 4]
num_dict = {}
res_list = []

for num in lst:
    if num_dict.get(num, 0):
        num_dict[num] += 1
    else:
        num_dict[num] = 1

print(num_dict)

for num, qty in num_dict.items():
    if qty > 1:
        res_list.append(num)
print(res_list)





