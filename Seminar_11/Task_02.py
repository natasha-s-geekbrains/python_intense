"""Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
При создании нового экземпляра класса старые данные из ранее
созданных экземпляров сохраняются в пару списков архивов.
List-архивы также являются свойствами экземпляра"""


class Archive:
    """Добавили документацию 'Та еще задачка'"""
    num_arch = []
    string_arch = []

    def __init__(self, num, string):
        """ Та еще функция в той еще задаче"""
        self.num = num
        self.text = string
        self.num_arch.append(num)
        self.string_arch.append(string)


a = Archive(5, 'gft')
print(a.num_arch)
b = Archive(2, 'od')
print(b.num_arch)
print(a.num_arch)
print(Archive.num_arch)


# print(Archive.__doc__)
# print(Archive.__init__.__doc__)
# print(help(Archive))



