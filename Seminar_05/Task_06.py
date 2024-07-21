"""✔ Выведите в консоль таблицу умножения
от 2х2 до 9х10 как на школьной тетрадке.
✔ Таблицу создайте в виде однострочного
генератора, где каждый элемент генератора —
отдельный пример таблицы умножения.
✔ Для вывода результата используйте «принт»
без перехода на новую строку."""

START_NUM = 2
END_NUM = 10
COLUMNS = 4
#
# for start_num_1 in (START_NUM, START_NUM + COLUMNS):
#     for num_2 in (range(START_NUM, END_NUM + 1, 1)):
#         for num_1 in range(start_num_1, start_num_1 + COLUMNS):
#             print(f'{num_1}  X {num_2:>2} = {num_1 * num_2:>2}', end='\t')
#         print()
#     print()

# for i in range(2, 11):
#     for j in range(2, 10):
#         print(f"{j}x{i}={j * i:2}", end='\t')
#     print()

# my_gen = (
#     (f"{j}x{i}={j * i:2}\t" for j in range(2, 10)) for i in range(2, 11)
# )
#
# print(*my_gen)

# my_gen = (
#     f'\n' if j == 11 else f' {j}*{i}={i * j:2d} ' for i in range(2, 10) for j in range(2, 12))
#
# print(*my_gen)
#
#
# [print(f"\n{i}x{j}={i*j}", end=" \t") for i in range(2, 10) '\n' for j in range(2, 11)]

# print(
#     *(("\t".join(f"{j:>2}x{i:>2}={j * i:>2}"
#                  for j in range(2, 10))
#                      for i in range(2, 11))), sep='\n'
# )


table = (
    f'\t{first_num:>2}*{second_num:>2}={first_num * second_num:>2}\t' if first_num != main_row + COLUMNS - 1 else
    f'{first_num:>2}*{second_num:>2}={first_num * second_num:>2}\n' if second_num != END_NUM else
    f'{first_num:>2}*{second_num:>2}={first_num * second_num:>2}\n\n'
    for main_row in (START_NUM, START_NUM + COLUMNS)
    for second_num in range(START_NUM, END_NUM + 1)
    for first_num in range(main_row, main_row + COLUMNS)
)

print(*table, end='')
