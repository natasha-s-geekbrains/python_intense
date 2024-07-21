"""✔ Создайте генератор чётных чисел от нуля до 100.
✔ Из последовательности исключите
числа, сумма цифр которых равна 8.
✔ Решение в одну строку."""

for i in range(0, 101, 2):
    if sum(map(int, str(i))) != 8:
        print(i)

print()

my_gen = (i for i in range(101) if (i % 2 == 0) & (i // 10 + i % 10 != 8))
print(*my_gen)

[print(i) for i in range(2, 101, 2) if sum(map(int, str(i))) != 8]


