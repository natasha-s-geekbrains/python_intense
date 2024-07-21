"""Создайте несколько переменных разных типов.
Проверьте к какому типу относятся созданные переменные.
"""

my_int = 10
my_float = 1.5
my_str = 'Hello world'
my_tuple = (1, 2, 3)

print(
    f'Объект {my_int=} имеет тип {type(my_int)}\n'
    f'Объект {my_float=} имеет тип {type(my_float)}\n'
    f'Объект {my_str=} имеет тип {type(my_str)}\n'
    f'Объект {my_tuple=} имеет тип {type(my_tuple)}'
)
