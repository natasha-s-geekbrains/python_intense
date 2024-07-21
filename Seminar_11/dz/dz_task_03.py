class Rectangle:
    def __init__(self, width, height=None):
        self.width = width
        self.height = height if height else width

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __add__(self, other):
        new_width = self.width + other.width
        new_perimeter = self.perimeter() + other.perimeter()
        new_height = int(new_perimeter / 2 - new_width)
        return Rectangle(new_width, new_height)

    # def __sub__(self, other):
    #     new_width = abs(self.width - other.width)
    #     new_area = abs(self.area() - other.area())
    #     new_height = new_area/new_width
    # return Rectangle(new_width, new_height)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        new_width = abs(self.width - other.width)
        new_perimeter = self.perimeter() - other.perimeter()
        new_height = int(new_perimeter/2 - new_width)
        return Rectangle(new_width, new_height)

    def __eq__(self, other):
        return self.area() == other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __str__(self):
        return f'Прямоугольник со сторонами {self.width} и {self.height}'

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"


# На входе (вар 1)
# rect1 = Rectangle(5, 10)
# rect2 = Rectangle(3, 7)
#
# print(f"Периметр rect1: {rect1.perimeter()}")
# print(f"Площадь rect2: {rect2.area()}")
# print(f"rect1 < rect2: {rect1 < rect2}")
# print(f"rect1 == rect2: {rect1 == rect2}")
# print(f"rect1 <= rect2: {rect1 <= rect2}")
#
# rect3 = rect1 + rect2
# print(f"Периметр rect3: {rect3.perimeter()}")
# rect4 = rect1 - rect2
# print(f"Ширина rect4: {rect4.width}")


# На входе (вар 2)
rect1 = Rectangle(4, 5)
rect2 = Rectangle(3, 3)

print(rect1)
print(rect2)

print(rect1.perimeter())
print(rect1.area())
print(rect2.perimeter())
print(rect2.area())

rect_sum = rect1 + rect2
rect_diff = rect1 - rect2

print(rect_sum)
print(rect_diff)

print(rect1 < rect2)
print(rect1 == rect2)
print(rect1 <= rect2)

print(repr(rect1))
print(repr(rect2))

# Периметр rect1: 30
# Площадь rect2: 21
# rect1 < rect2: False
# rect1 == rect2: False
# rect1 <= rect2: False
# Периметр rect3: 50
# Ширина rect4: 2


# Прямоугольник со сторонами 4 и 5
# Прямоугольник со сторонами 3 и 3
# 18
# 20
# 12
# 9
# Прямоугольник со сторонами 7 и 8
# Прямоугольник со сторонами 1 и 2
# False
# False
# False
# Rectangle(4, 5)
# Rectangle(3, 3)
