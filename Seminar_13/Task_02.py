"""Создайте функцию аналог get для словаря.
Помимо самого словаря функция принимает ключ и
значение по умолчанию.
При обращении к несуществующему ключу функция должна
возвращать дефолтное значение.
Реализуйте работу через обработку исключений.
"""


def get_dict(cur_dict, key, default_value=0):
    try:
        if not isinstance(cur_dict, dict):
            raise TypeError
    except TypeError as te:
        return 'Аргумент не является словарем'
    try:
        return cur_dict[key]
    except KeyError as e:
        return default_value


if __name__ == '__main__':
    my_dict = {'1': 1, '2': 2, '3': 3}
    print(get_dict(my_dict, '1'))
    print(get_dict(my_dict, '4'))
    print(get_dict(my_dict, '4', None))
    new_dict = 5
    print(get_dict(new_dict, 1))
