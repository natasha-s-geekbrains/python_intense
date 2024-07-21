"""Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
имена str, ставка int, премия str с указанием процентов вида 10.25%.
В результате result получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии.
Не забудьте распечатать в конце результат.
names = ["Alice", "Bob", "Charlie"]
salary = [5000, 6000, 7000]
bonus = ["10%", "5%", "15%"]

{'Alice': 500.0, 'Bob': 300.0, 'Charlie': 1050.0}
"""


names = ["Alice", "Bob", "Charlie"]
salary = [5000, 6000, 7000]
bonus = ["10%", "5%", "15%"]

result = dict(
        map(
            lambda cur_tuple: (
                cur_tuple[0], cur_tuple[1] * float(cur_tuple[2][:-1]) / 100
            ), zip(names, salary, bonus)
        )
    )

print(result)

# РЕШЕНИЕ GB


result = {names[i]: round(salary[i] * float(bonus[i].strip('%')) / 100, 2) for i in range(len(names))}
print(result)
