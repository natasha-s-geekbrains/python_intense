"""Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании
экземпляра.
У класса должно быть два метода, возвращающие периметр
и площадь.
Если при создании экземпляра передаётся только одна
сторона, считаем что у нас квадрат.
"""


class Rectangle:
    def __init__(self, length, width=None):
        self.length = length
        self.width = width if width else length

    def square(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


if __name__ == '__main__':
    rect_1 = Rectangle(2, 5)
    rect_2 = Rectangle(5)

    print(rect_1.square())
    print(rect_1.perimeter())

    print(rect_2.square())
    print(rect_2.perimeter())
