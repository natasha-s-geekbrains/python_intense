"""Создайте функцию, которая запрашивает числовые данные от
пользователя до тех пор, пока он не введёт целое или
вещественное число.
Обрабатывайте не числовые данные как исключения."""


def get_num():
    while True:
        num = input('Ведите целое или вещественное число: ')
        try:
            return int(num)
        except ValueError as e:
            try:
                return float(num)
            except ValueError as e:
                print('Неверный формат введенного числа. Повторите ввод.')


def get_num2():
    while True:
        num = input('Ведите целое или вещественное число: ')
        try:
            return float(num)
        except ValueError as e:
            print('Неверный формат введенного числа. Повторите ввод.')


def get_num3():
    while True:
        num = input('Ведите целое или вещественное число: ')
        try:
            res = float(num)
            break
        except ValueError as e:
            print('Неверный формат введенного числа. Повторите ввод.')
    try:
        res = int(num)
    except ValueError as e:
        pass
    return res


if __name__ == '__main__':
    # print(get_num())
    # print(get_num2())
    res_num = get_num3()
    print(res_num)
