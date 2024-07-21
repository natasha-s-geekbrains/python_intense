"""✔ Создайте функцию-генератор.
✔ Функция генерирует N простых чисел,
начиная с числа 2.
✔ Для проверки числа на простоту используйте
правило: «число является простым, если делится
нацело только на единицу и на себя»"""


def my_gen(num):
    start = 2
    count = 0
    while count < num:
        for i in range(2, int(start ** 0.5 + 1)):
            if start % i == 0:
                break
        else:
            count += 1
            yield start
        start += 1


N = 5

for num in my_gen(N):
    print(num)

# my_iter = iter(my_gen(N))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))


