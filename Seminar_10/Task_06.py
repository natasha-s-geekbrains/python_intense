"""Доработайте задачу 5.
Вынесите общие свойства и методы классов в класс
Животное.
Остальные классы наследуйте от него.
Убедитесь, что в созданные ранее классы внесены правки."""


class Animal:
    def __init__(self, type_name, age):
        self.type_name = type_name
        self.age = age


class Fish(Animal):
    def __init__(self, type_name, age, max_deep):
        super().__init__(type_name, age)
        self.max_deep = max_deep

    def get_max_deep(self):
        if self.max_deep < 10:
            return 'Мелководная рыба'
        else:
            return 'Глубоководная рыба'


class Bird(Animal):
    def __init__(self, type_name, age, wingspan):
        super().__init__(type_name, age)
        self.wingspan = wingspan

    def wing_length(self):
        return f'Размах крыла = {self.wingspan / 2}'


class Mammal(Animal):
    def __init__(self, type_name, age, weight):
        super().__init__(type_name, age)
        self.weight = weight

    def get_weight(self):
        if self.weight < 100:
            return 'Мелкий зверь'
        else:
            return 'Крупный зверь'


if __name__ == '__main__':
    fish_1 = Fish('Карась Вася', '1 год', 3)
    print(fish_1)
    print(fish_1.get_max_deep())

    bird_1 = Bird('Орел Петя', '2 года', 2)
    print(bird_1.wing_length())

    mammal_1 = Mammal('Ишак Моисей', '2 года', 200)
    print(f'{fish_1.type_name} {fish_1.age} {fish_1.get_max_deep()}')


