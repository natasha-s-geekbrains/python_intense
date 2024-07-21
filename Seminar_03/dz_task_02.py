"""В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов.
Слова разделяются пробелами. Такие слова как don t, it s, didn t итд
(после того, как убрали знак препинания апостроф) считать двумя словами.
Цифры за слова не считаем.
Отсортируйте по убыванию значения количества повторяющихся слов. Слова выведите в обратном алфавитном порядке.
text = 'Hello world. Hello Python. Hello again.'
[('hello', 3), ('world', 1), ('python', 1), ('again', 1)]
text = 'This is a sample text without repeating words.'
[('words', 1), ('without', 1), ('this', 1), ('text', 1), ('sample', 1), ('repeating', 1), ('is', 1), ('a', 1)]
text = 'Python 3.9 is the latest version of Python. It's awesome!'
[('python', 2), ('version', 1), ('the', 1), ('s', 1), ('of', 1), ('latest', 1), ('it', 1), ('is', 1), ('awesome', 1)]
text = 'The quick brown fox jumps over the lazy dog. Lazy dog, lazy fox!'
[('lazy', 3), ('the', 2), ('fox', 2), ('dog', 2), ('quick', 1), ('over', 1), ('jumps', 1), ('brown', 1)
"""

import re

text = "Python 3.9 is the latest version of Python. It's awesome!"
words_dict = {}

# step 1 - clear text
text = re.sub('[!@#$\n-.,]', ' ', text).lower()
words = text.split()
words.sort(reverse=True)
print(f'words: {words}')

# step 2 - count words repetition

for word in words:
    if word.isdigit():
        continue
    elif words_dict.get(word, 0):
        words_dict[word] += 1
    else:
        words_dict[word] = 1
print(f'words_dict: {words_dict}')

# step 3 - sort dict

sorted_words_dict = sorted(
    words_dict.items(), key=lambda tpl: tpl[1], reverse=True
)

print(f'sorted_words_dict: {sorted_words_dict}')
