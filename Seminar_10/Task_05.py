"""Создайте три (или более) отдельных классов животных.
Например, рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства,
например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий
информацию специфичную для данного класса."""


class Fish:
    def __init__(self, type_name, age, max_deep):
        self.type_name = type_name
        self.age = age
        self.max_deep = max_deep

    def get_max_deep(self):
        if self.max_deep < 10:
            return 'Мелководная рыба'
        else:
            return 'Глубоководная рыба'


class Bird:
    def __init__(self, type_name, age, wingspan):
        self.type_name = type_name
        self.age = age
        self.wingspan = wingspan

    def get_wing(self):
        return f'Размах крыла = {self.wingspan / 2}'


class Mammal:
    def __init__(self, type_name, age, weight):
        self.type_name = type_name
        self.age = age
        self.weight = weight

    def get_weight(self):
        if self.weight < 100:
            return 'Мелкий зверь'
        else:
            return 'Крупный зверь'



