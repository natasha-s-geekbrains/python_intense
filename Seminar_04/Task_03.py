""" Функция получает на вход строку из двух чисел через пробел.
✔ Сформируйте словарь, где ключом будет
символ из Unicode, а значением — целое число.
✔ Диапазон пар ключ-значение от наименьшего из введённых
пользователем чисел до наибольшего включительно."""


def my_func(text: str) -> dict[str, int]:
    """Documentation."""
    num_min, num_max = sorted(map(int, text.split()))
    return {chr(num): num for num in range(num_min, num_max + 1)}


print(my_func('25 53'))
