"""Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения
возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого
изменения, но есть возможность получить текущий возраст."""


class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.__age = age

    def birthday(self):
        self.__age += 1

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_age(self):
        return self.__age


if __name__ == '__main__':
    user_1 = User('A', 'B', 20)
    user_2 = User('C', 'D', 35)

    print(user_1.full_name())
    print(user_1.get_age())

    print(user_2.full_name())
    print(user_2.get_age())

    user_1.birthday()
    user_2.birthday()

    print(user_1.get_age())
    print(user_2.get_age())
