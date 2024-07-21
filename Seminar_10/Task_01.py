"""Создайте класс окружность.
Класс должен принимать радиус окружности при создании
экземпляра.
У класса должно быть два метода, возвращающие длину
окружности и её площадь."""

from math import pi


class Circle:

    def __init__(self, radius=12):
        self.radius = radius

    def square(self):
        return pi * self.radius ** 2

    def length(self):
        return 2 * pi * self.radius


if __name__ == '__main__':
    circle_1 = Circle(10)
    circle_2 = Circle(20)
    circle_3 = Circle()

    print(f'{circle_1.square()=}')
    print(f'{circle_1.length()=}')

    print(f'{circle_2.square()=}')
    print(f'{circle_2.length()=}')

    print(f'{circle_3.square()=}')
    print(f'{circle_3.length()=}')
