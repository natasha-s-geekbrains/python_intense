"""Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
При создании нового экземпляра класса старые данные из ранее
созданных экземпляров сохраняются в пару списков архивов.
List-архивы также являются свойствами экземпляра"""


class Archive:
    """Добавили документацию 'Та еще задачка'"""
    _instance = None

    def __new__(cls, num, string):
        """Функция __new__ в той еще задаче"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_nums = []
            cls._instance.archive_strings = []
        else:
            cls._instance.archive_nums.append(cls._instance.num)
            cls._instance.archive_strings.append(cls._instance.string)
        return cls._instance

    def __init__(self, num, string):
        """Функция __init__ в той еще задаче"""
        self.num = num
        self.string = string


a = Archive(5, 'gft')
print(a.archive_nums)
b = Archive(2, 'od')
print(b.archive_nums)
print(a.archive_nums)
c = Archive(8, 'ghjhk')
print(c.archive_nums)
print(b.archive_nums)
print(a.archive_nums)

print(Archive.__doc__)
print(Archive.__init__.__doc__)
print(Archive.__new__.__doc__)
print(help(Archive))

