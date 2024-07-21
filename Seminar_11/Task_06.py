"""Доработайте прошлую задачу.
Добавьте сравнение прямоугольников по площади
Должны работать все шесть операций сравнения
"""


class Rectangle:
    def __init__(self, length, width=None):
        self.length = length
        self.width = width if width else length

    def square(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def __add__(self, other):
        new_width = self.width + other.width
        new_perimeter = self.perimeter() + other.perimeter()
        new_length = new_perimeter / 2 - new_width
        return Rectangle(new_length, new_width)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        new_width = abs(self.width - other.width)
        new_perimeter = self.perimeter()-other.perimeter()
        new_length = int(new_perimeter/2 - new_width)
        return Rectangle(new_length, new_width)

    # def __sub__(self, other):
    #     new_width = abs(self.width - other.width)
    #     new_area = abs(self.area() - other.area())
    #     new_height = new_area/new_width
    # return Rectangle(new_width, new_height)

    def __eq__(self, other):
        return self.square() == other.square()

    def __gt__(self, other):
        return self.square() > other.square()

    def __le__(self, other):
        return self.square() <= other.square()


a = Rectangle(25, 5)
b = Rectangle(24, 9)
c = a - b

print(c.perimeter(), c.length, c.width)
print(a.square(), b.square())
print(a == b)
print(a != b)
print(a <= b)
print(a >= b)
print(a < b)
print(a > b)
