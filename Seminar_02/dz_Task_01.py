"""Напишите программу, которая получает целое число num
и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
num = 255
Шестнадцатеричное представление числа: FF
Проверка результата: 0xff

"""

num = int(input('Enter integer number: \n'))

num_hex = '' if num == 0 else hex(num)[2:].upper()

print(
    f'Шестнадцатеричное представление числа: {num_hex}\n'
    f'Проверка результата: {hex(num)}'
)

num_str = hex(num)
print(type((hex(num)[2:]).upper()))
print(type(hex(num)))

print('\nCHECKING:')
print(type(num))
print(int(num_str, base=16))

print('\nBEST PRACTICE:')

HEX = 16
hex_digits = "0123456789ABCDEF"

hex_num = ""
test_hex_num = hex(num)

while num > 0:
    remainder = num % HEX
    print(remainder)
    hex_num = hex_digits[remainder] + hex_num
    print(hex_num)
    num //= HEX
    print(num)

print("Шестнадцатеричное представление числа:", hex_num)
print("Проверка результата:", test_hex_num)


