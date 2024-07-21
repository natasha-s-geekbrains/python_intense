"""Напишите функцию группового переименования файлов
в папке test_folder под названием rename_files. Она должна:
a) принимать параметр желаемое конечное имя файлов desired_name;
при переименовании в конце имени добавляется порядковый номер
b) принимать параметр количество цифр в порядковом номере num_digits
c) принимать параметр расширение исходного файла source_ext
Переименование должно работать только для этих файлов внутри каталога
d) принимать параметр расширение конечного файла target_ext
e) принимать диапазон сохраняемого оригинального имени.
Например, для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
К ним прибавляется желаемое конечное имя, если оно передано.
Далее счётчик файлов и расширение.
f. Папка test_folder доступна из текущей директории.
На входе:
rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")
На выходе:
new_file_008.doc, test.doc, new_file_004.doc, new_file_005.doc, new_file_007.doc, new_file_001.doc, new_file_006.doc, \
new_file_003.doc, new_file_002.doc, new_file_009.doc, new_file_010.doc
"""


__all__ = ['rename_files']

import os


def rename_files(desired_name: str, num_digits: int, source_ext: str, target_ext: str) -> None:
    path = 'test_folder'
    files = os.listdir(path)
    target_files_str = ''
    other_files_str = ''
    counter = 0

    for i, file_name in enumerate(files):
        ext = os.path.splitext(file_name)[1]

        folder_name = 'test_folder'
        folder_path = os.path.join(os.getcwd(), folder_name)

        if ext == '.' + source_ext:
            new_name = '{}{:0{}}.{}'.format(desired_name, i + 1 + counter, num_digits, target_ext)

            old_path = os.path.join(folder_path, file_name)
            new_path = os.path.join(folder_path, new_name)
            os.rename(old_path, new_path)
            target_files_str += f'{new_name}, '
        else:
            counter -= 1
            other_files_str += f'{file_name}, '

    print(target_files_str + other_files_str)
    files = os.listdir(path)
    print(files)


if __name__ == '__main__':
    rename_files(desired_name="new_file_", num_digits=3, source_ext="doc", target_ext="txt")
