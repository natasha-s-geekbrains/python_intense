"""Доработаем класс Архив из задачи 2.
Добавьте методы представления экземпляра для программиста
и для пользователя."""


class Archive:
    """Добавили документацию 'Та еще задачка'"""
    num_arch = []
    string_arch = []

    def __init__(self, num, string):
        """ Та еще функция в той еще задаче"""
        self.num = num
        self.string = string
        self.num_arch.append(num)
        self.string_arch.append(string)

    def __str__(self):
        """ Инфо для юзера"""
        return f'Number: {self.num}, String: {self.string}, Archive: {list(zip(self.num_arch, self.string_arch))}'

    def __repr__(self):
        """ Инфо для разработчика"""
        return f'Archive: {self.num}, {self.string}'


a = Archive(5, 'gft')
b = Archive(2, 'od')

print(a)
print(repr(b))






