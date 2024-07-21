"""
Пользователь вводит данные. Сделайте проверку данных
и преобразуйте если возможно в один из вариантов ниже:
✔ Целое положительное число
✔ Вещественное положительное или отрицательное число
✔ Строку в нижнем регистре, если в строке есть
хотя бы одна заглавная буква
✔ Строку в верхнем регистре в остальных случаях
"""


user_input = input('Enter data: ')

if user_input.isdigit():
    user_input = int(user_input)
elif user_input.replace('-', '').replace('.', '').isdigit() and \
        user_input.count('.') < 2 and '-' not in user_input[1:]:
    user_input = float(user_input)
elif user_input.lower() != user_input:
    user_input = user_input.lower()
else:
    user_input = user_input.upper()

print(user_input)
