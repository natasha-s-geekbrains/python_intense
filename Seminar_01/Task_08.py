"""Нарисовать в консоли ёлку спросив
у пользователя количество рядов.
Пример результата:
Сколько рядов у ёлки? 5
 *
 ***
 *****
 *******
*********"""


SPACE = ' '
STAR = '*'

rows_num = int(input('Enter number of rows: '))
spaces = rows_num - 1
stars = 1

for _ in range(rows_num):
    print(f'{SPACE * spaces}{STAR * stars}')
    stars += 2
    spaces -= 1


