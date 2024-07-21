"""Дорабатываем класс прямоугольник из прошлого семинара.
Добавьте возможность сложения и вычитания.
При этом должен создаваться новый экземпляр
прямоугольника.
Складываем и вычитаем периметры, а не длину и ширину.
При вычитании не допускайте отрицательных значений.
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

    # def __sub__(self, other):
    #     new_width = abs(self.width - other.width)
    #     new_square = abs(self.square() - other.square())
    #     print(self.square(), new_square)
    #     new_length = new_square/new_width
    #     return Rectangle(new_length, new_width)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        new_width = abs(self.width - other.width)
        new_perimeter = self.perimeter() - other.perimeter()
        new_height = int(new_perimeter/2 - new_width)
        return Rectangle(new_width, new_height)


a = Rectangle(25, 5)
print(a.perimeter())
b = Rectangle(24, 9)
print(b.perimeter())
c = a - b

print(c.perimeter(), c.length, c.width)

