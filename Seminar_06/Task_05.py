"""Добавьте в модуль с загадками функцию, которая хранит
словарь списков.
� Ключ словаря - загадка, значение - список с отгадками.
� Функция в цикле вызывает загадывающую функцию, чтобы
передать ей все свои загадки."""


# def secrets(riddle: str, answers: list[str], attempts: int = 3) -> int:
#     print(f'Угадай загадку:\n{riddle}\n')
#     for attempt in range(1, attempts + 1):
#         answer = input(f'Попытка №{attempt}:\n').lower()
#         if answer in answers:
#             return attempt
#     return 0
#
#
# def riddle_storage():
#     my_dict = {
#         'Зимой и летом одним цветом': ['елка', 'ель', 'сосна'],
#         'Кто меня раздевает, тот слезы проливает': ['лук', 'луковица'],
#         'Летом серый, зимой белый': ['заяц', 'зайчик']
#     }
#     for key, value in my_dict.items():
#         result = secrets(key, value)
#         print(f'Угадал с попытки {result}' if result > 0 else 'Не угадал!')
#
#
# if __name__ == '__main__':
#     riddle_storage()

    # CHECK


def secrets(riddle: str, answers: list[str], attempts: int = 3) -> int:
    print(f"Угадайте загадку:\n{riddle}\n")
    for attempt in range(1, attempts + 1):
        answer = input(f"Попытка № {attempt}\n").lower()
        if answer in answers:
            return attempt
    return 0


def riddle_storage():
    my_dict = {
        'Зимой и летом одним цветом': ['ель', 'ёлка', 'сосна'],
        'Кто меня раздевает, тот слезы проливает': ['лук', 'луковица'],
        'Летом серый, зимой белый': ['заяц', 'зайчик']
    }
    for key, value in my_dict.items():
        result = secrets(key, value)
        print(f"Угадал с попытки {result}\n" if result > 0 else "Не угадал\n")


if __name__ == '__main__':
    riddle_storage()
