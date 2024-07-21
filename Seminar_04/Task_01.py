"""Напишите функцию, которая принимает строку текста.
Вывести функцией каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого
длинного слова был один пробел между ним и номером строки. """


def print_words(text):
    words = sorted(text.split())
    max_len = len(max(words, key=len))

    for i, word in enumerate(words, 1):
        # print(f'{i: >3} {word: >{max_len}}')
        print(str(i).rjust(3), word.rjust(max_len))


input_text = input('Введите произвольный текст: \n')
print_words(input_text)
