"""Создайте функцию генератор чисел Фибоначчи fibonacci.
f = fibonacci()
for i in range(10):
    print(next(f))
0
1
1
2
3
5
8
13
21
34
"""


def fibonacci():
    first = 1
    second = 0
    while True:
        yield second
        first, second = second, second + first


f = fibonacci()
for j in range(10):
    print(next(f))
