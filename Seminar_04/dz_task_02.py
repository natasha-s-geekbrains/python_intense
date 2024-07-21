"""Напишите функцию key_params,
принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ - значение переданного аргумента, а значение - имя аргумента.
Если ключ не хешируем, используйте его строковое представление.

params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
print(params)

{1: 'a', 'hello': 'b', '[1, 2, 3]': 'c', '{}': 'd'}"""


# def key_params(**kwargs) -> dict:
#     res_dict = {}
#     for key, value in kwargs.items():
#         if isinstance(key, (dict, list, set)):
#             res_dict[str(key)] = key
#         else:
#             res_dict[value] = key
#     return res_dict

def key_params(**kwargs) -> dict:
    res_dict = {}
    for key, value in kwargs.items():
        res_dict[value if value.__hash__ is not None else str(value)] = key
    return res_dict


# for i, item in enumerate(data, start=1):
#     check_int = 'Это число' if isinstance(item, int) else ''
#     check_str = 'Это строка' if isinstance(item, str) else ''
#     # check_hash = 'не хэшируем' if isinstance(item, (dict, list, set)) else hash(item)
#     # check_hash = 'не хэшируем' if isinstance(item, (typing.Hashable) else hash(item)


params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
print(params)
