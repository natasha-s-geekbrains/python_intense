"""Добавьте в модуль с загадками функцию, которая
принимает на вход: строку (текст загадки) и число (номер
попытки, с которой она угадана).
� Функция формирует словарь с информацией о результатах
отгадывания.
� Для хранения используйте защищённый словарь уровня
модуля.
� Отдельно напишите функцию, которая выводит результаты
угадывания из защищённого словаря в удобном для чтения
виде.
� Для формирования результатов используйте генераторное
выражение."""

__all__ = ['show_results']

_data_dict = {}


def secrets(riddle: str, answers: list[str], attempts: int = 3) -> int:
    print(f"Угадайте загадку:\n{riddle}\n")
    for attempt in range(1, attempts + 1):
        answer = input(f"Попытка № {attempt}\n").lower()
        if answer in answers:
            return attempt
    return 0


def save(puzzle: str, count: int) -> {}:
    _data_dict.update({puzzle: count})


def riddle_storage():
    my_dict = {
        'Зимой и летом одним цветом': ['ель', 'ёлка', 'сосна'],
        'Кто меня раздевает, тот слезы проливает': ['лук', 'луковица'],
        'Летом серый, зимой белый': ['заяц', 'зайчик']
    }
    for key, value in my_dict.items():
        result = secrets(key, value)
        save(key, result)
        print(f"Угадал с попытки {result}\n" if result > 0 else "Не угадал\n")


def show_results():
    result = (
        f'Загадку {key} разгадали с попытки {value}' if value > 0
        else f'Загадку {key} не разгадали'
        for key, value in _data_dict.items()
    )
    print('\n'.join(result))


if __name__ == '__main__':
    riddle_storage()
    show_results()
