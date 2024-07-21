"""Задание №6.
Напишите код, который запускается из командной строки и получает на вход
путь до директории на ПК.
Соберите информацию о содержимом в виде объектов namedtuple.
Каждый объект хранит:
○ имя файла без расширения или название каталога,
○ расширение, если это файл или флаг каталога, если это каталог
○ название родительского каталога.
В процессе сбора сохраните данные в текстовый файл используя
логирование.
"""

import argparse
from pathlib import Path
import logging
from collections import namedtuple

FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
         'в строке {lineno:03d} функция "{funcName}()" ' \
         'в {created} секунд записала сообщение: {msg}'

logging.basicConfig(format=FORMAT, style='{', level=logging.INFO, filemode='a', filename='info_1.log',
                    encoding='utf-8')

logger = logging.getLogger('Task_06')
File = namedtuple('File', 'name, extension, dir, parent')


def read_dir(path):
    for item in path.iterdir():
        obj_name, obj_ext = None, None
        obj = File(item.stem if item.is_file() else item.name, item.suffix, item.is_dir, item.parent)
        logger.info(obj)


def parse_dir():
    parser = argparse.ArgumentParser(description='Получает путь к директории', prog='date_find()',
                                     epilog='Возвращает дату')

    parser.add_argument('-p', '--path', help="Введите путь к директории", required=True, type=Path)
    args = parser.parse_args()
    return read_dir(args.path)


if __name__ == '__main__':
    parse_dir()
