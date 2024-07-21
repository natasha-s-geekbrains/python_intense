"""✔ Функция принимает на вход три списка одинаковой длины:
✔ имена str,
✔ ставка int,
✔ премия str с указанием процентов вида «10.25%».
✔ Вернуть словарь с именем в качестве ключа и суммой
премии в качестве значения.
✔ Сумма рассчитывается как ставка умноженная на процент премии."""


def my_func(
        names: list[str] = ['Vasya'], /,
        salaries: list[int] = [10_000], *,
        bonuses: list[str] = ['10%']
) -> dict:
    """Documentation."""
    # return {
    #     name: salary * float(bonus[:-1]) / 100
    #     for name, salary, bonus in zip(names, salaries, bonuses)
    # }
    return dict(
        map(
            lambda cur_tuple:
            (cur_tuple[0],
             cur_tuple[1] * float(cur_tuple[2][:-1]) / 100),
            zip(names, salaries, bonuses)
        )
    )


names_out = ['Иванов', 'Петров', 'Сидоров']
rates_out = [10_000, 12_000, 15_000]
awards_out = ['15.75%', '12.50%', '10.25%']


print(my_func(names_out, salaries=rates_out, bonuses=awards_out))