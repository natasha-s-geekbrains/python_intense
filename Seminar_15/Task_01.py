"""Задание №1.
Напишите программу, которая использует модуль logging для
вывода сообщения об ошибке в файл.
Например, отлавливаем ошибку деления на ноль.
logging.basicConfig
# filename	Указывает, что вместо `StreamHandler` должен быть создан `FileHandler` с использованием указанного имени файла.
# filemode	Если указано имя файла, открывает файл в этом режиме. По умолчанию `а` - добавление записей в журнал.
# format	Использует указанную строку формата для обработчика.
# datefmt	Использует указанный формат даты/времени, принятый в функции `time.strftime()`.
# style	Если указан аргумент `format`, то использует этот стиль для строки формата. Один из '%', '{' или '$' для стиля форматирования `printf`, `str.format()` или `string.Template` соответственно. По умолчанию используется значение '%'.
# level	Устанавливает уровень корневого регистратора на указанный уровень логирования.
# stream	Использует указанный поток для инициализации `StreamHandler`. Обратите внимание, что этот аргумент несовместим с именем файла. Если присутствуют оба, то возникает `ValueError`.
# handlers	Если указано, то это должен быть итератор из уже созданных обработчиков для добавления в корневой регистратор `logger`. Любым обработчикам, у которых еще не установлен форматер, будет назначен форматер по умолчанию, созданный в этой функции. Обратите внимание, что этот аргумент несовместим с именем файла `filename` или потоком `stream`. Если присутствуют оба, возникает `ValueError`.
# force	Если этот ключевой аргумент задан как `True`, то любые существующие обработчики, подключенные к корневому регистратору, удаляются и закрываются перед выполнением конфигурации с новыми аргументами."""

import logging
import os

current_file = os.path.realpath(__file__)
path = f'\'{current_file}\''
log_file_name = os.path.splitext(os.path.basename(path))[0]

FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
         'в строке {lineno:03d} функция "{funcName}()" ' \
         'в {created} секунд записала сообщение: {msg}'

logging.basicConfig(format=FORMAT, style='{', level=logging.NOTSET, filemode='a', filename='error_test.log',
                    encoding='utf-8')

logger = logging.getLogger(f'{log_file_name}')


def div_func(a, b):
    res = float('inf')
    try:
        res = a / b
    except ZeroDivisionError:
        logger.error(f'b = {b}. На ноль делить нельзя')
    return res


if __name__ == '__main__':
    print(div_func(3, 0))