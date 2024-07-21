"""Создайте класс Моя Строка, где:
- будут доступны все возможности str
- дополнительно хранятся имя автора строки и время создания (time.time)"""

import time


class MyStr(str):

    def __init__(self, *args, **kwargs):
        print('Сработал метод __init__', args)

    def __new__(cls, text, author):
        instance = super().__new__(cls, text)
        instance.author = author
        instance.time = time.time()
        print('Сработал метод __new__', instance.author, instance.time, instance)
        return instance


print('Начало программы')

a = MyStr('hello', 'Pushkin')
b = MyStr('bye', 'Pupkin')
c = MyStr('goodBye', 'Klein')
d = MyStr('bu-bu-bu', 'people')
e = a

print(a, a.author, a.time)
print(a, b, c, d, e)
print(a.author, b.time, c, d.author, e.author)
