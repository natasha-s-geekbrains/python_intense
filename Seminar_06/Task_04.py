"""Создайте модуль с функцией внутри.
� Функция получает на вход загадку, список с возможными
вариантами отгадок и количество попыток на угадывание.
� Программа возвращает номер попытки, с которой была
отгадана загадка или ноль, если попытки исчерпаны."""


def secrets(riddle: str, answers: list[str], attempts: int = 3) -> int:
    print(f'Угадай загадку:\n{riddle}\n')
    for attempt in range(1, attempts + 1):
        answer = input(f'Попытка №{attempt}:\n').lower()
        if answer in answers:
            return attempt
    return 0


if __name__ == '__main__':
    my_answers = ['елка', 'ель', 'сосна']
    result = secrets('Зимой и летом одним цветом', my_answers, 3)
    print(f'Угадал с попытки {result}' if result>0 else 'Не угадал!')



