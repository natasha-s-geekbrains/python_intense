"""✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
✔ Напишите функцию, которая при запуске заменяет содержимое переменных
оканчивающихся на s (кроме переменной из одной буквы s) на None.
✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце."""


def my_func():
    dict_vars = globals()
    dict_new_vars = {}
    for key, value in dict_vars.items():
        if key[-1] == 's' and key != 's':
            dict_new_vars[key[:-1]] = value
            dict_vars[key] = None
    dict_vars.update(dict_new_vars)


datas = [42, -73, 12, 85, -15, 2]
s = 'Hello world!'
names = ('NoName', 'OtherName', 'NewName')
sx = 42

print(globals())
my_func()
print(globals())
print(datas, s, names, sx)
# print(name, data)
