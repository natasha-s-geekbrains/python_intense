"""Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
Под "успешной расстановкой ферзей" в данном контексте
подразумевается такая расстановка ферзей на шахматной доске,
в которой ни один ферзь не бьет другого.
Другими словами, ферзи размещены таким образом,
что они не находятся на одной вертикали, горизонтали или диагонали.
Список из 4-х комбинаций координат сохраните в board_list. Дополнительно печатать его не надо.
print(generate_boards())
[
[(1, 4), (2, 7), (3, 1), (4, 8), (5, 5), (6, 2), (7, 6), (8, 3)],
[(1, 5), (2, 3), (3, 8), (4, 4), (5, 7), (6, 1), (7, 6), (8, 2)],
[(1, 3), (2, 6), (3, 8), (4, 2), (5, 4), (6, 1), (7, 7), (8, 5)],
[(1, 6), (2, 1), (3, 5), (4, 2), (5, 8), (6, 3), (7, 7), (8, 4)]
]
"""

import random
from itertools import combinations


def generate_board():
    # Генерируем случайную доску
    q_board = []

    for i in range(1, 8+1):
        queen = (i, random.randint(1, 8))
        q_board.append(queen)
    return q_board


def is_attacking(q1, q2):
    # Проверяем, бьют ли ферзи друг друга
    return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])


def check_queens(queens_board):
    # Проверяем все возможные пары ферзей
    for q1, q2 in combinations(queens_board, 2):
        if is_attacking(q1, q2):
            return False
    return True


def generate_boards():
    # Генерируем доски, пока не получим 4 успешные расстановки
    count = 0
    board_list = []
    while count < 4:
        q_board = generate_board()
        if check_queens(q_board):
            count += 1
            board_list.append(q_board)
    return board_list


print(generate_boards())
