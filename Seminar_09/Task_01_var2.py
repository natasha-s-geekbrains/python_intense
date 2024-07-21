"""Создайте функцию-замыкание.
Функция запрашивает два целых числа:
○ от 1 до 100 для загадывания,
○ от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит
угадать загаданное число за указанное число попыток."""


def guessing_game(guessing: int, attempts: int):
    def wrapper():
        nonlocal attempts
        for i in range(attempts):
            print(f'Попытка #{i+1}')
            var = int(input('Угадай число: '))
            if var == guessing:
                return 'Вы угадали, браво!!'
        return 'Количество попыток исчерпано'

    return wrapper


if __name__ == '__main__':
    game1 = guessing_game(10, 5)
    print(game1())

