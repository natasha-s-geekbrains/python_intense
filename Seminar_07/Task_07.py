"""✔ Создайте функцию для сортировки файлов по директориям:
видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы,
которые не подошли для сортировки.
"""
import os

import Task_06 as tsk
from pathlib import Path


def sort_files(path: Path | str, groups: dict[Path, list[str]] = None) -> None:
    if groups is None:
        groups = {
            Path('video'): list['avi', 'mkv'],
            Path('pic'): list['png', 'jpg'],
            Path('music'): list['mp3']
        }
    if isinstance(path, str):
        path = Path(path)

    os.chdir(path)
    for target_dir, ext_list in groups.items():
        if not target_dir.is_dir():
            target_dir.mkdir()
        for file in list(os.walk(Path.cwd()))[0][-1]:
            if file.split('.')[-1] in ext_list:
                os.replace(file, os.path.join(target_dir, file))


# tsk.gen_files(r'C:\Users\iru\PycharmProjects\pythonProject1\Seminar_07\ex1\test', avi=2, mkv=1, png=2, mp3=2, jpg=2)
variable = r'C:\Users\iru\PycharmProjects\pythonProject1\Seminar_07\ex1\test'
sort_files(variable)
