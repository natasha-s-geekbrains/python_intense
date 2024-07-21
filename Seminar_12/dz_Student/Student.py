import csv


class Text:
    """
    Класс дескриптор, который проверяет ФИО студента на правила написания
    """

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __set__(self, instance, value):
        if not value.istitle() or not value.replace(' ', '').isalpha():
            print(value)
            raise ValueError(f'ФИО должно состоять только из букв и начинаться с заглавной буквы')
        else:
            setattr(instance, self.param_name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)


class Student:
    """
    Класс, который будет представлять студента и его успехи по предметам.
    Атрибуты класса:
    name (str): ФИО студента
    subjects (dict): Словарь, который хранит предметы в качестве ключей
    и информацию об оценках и результатах тестов для каждого предмета в виде словаря.
    Оценки отдельно, а результаты тестов - отдельно.
    """

    name = Text()

    def __init__(self, name: str, subjects_file: str):
        """
        Конструктор класса. Принимает имя студента и файл с предметами и их результатами.
        Инициализирует атрибуты name и subjects и вызывает метод load_subjects
        для загрузки предметов из файла.
        {Предмет_1: [{Оценки: [3, 2, 5, 4]}, {Результаты тестов: [85, 100, 0, 92]}]
        {Предмет_2: [{Оценки: [2, 5, 3, 4]}, {Результаты тестов: [71, 12, 0, 100]}]
        """

        self.name = name
        self.subjects = self.load_subjects(subjects_file)

    def load_subjects(self, subjects_file):
        """
        Метод для загрузки предметов из файла
        """

        with open(subjects_file, 'r', encoding='utf-8', newline='') as file_read:
            reader = csv.reader(file_read)

            subjects = {}

            for row in reader:
                for subject in row:
                    subjects[subject] = {'Оценки': [], 'Результаты тестов': []}

            return subjects

    def __setattr__(self, name, value):
        """
        Дескриптор, который проверяет установку атрибута name.
        Убеждается, что name начинается с заглавной буквы и состоит только из букв.
        Если ФИО не соответствует условию, выведите:
        'ФИО должно состоять только из букв и начинаться с заглавной буквы'
        """

        if name == 'name':
            super().__setattr__(name, value)
        else:
            self.__dict__[name] = value

    def __getattr__(self, name):
        """
        Позволяет получать значения атрибутов предметов
        (оценок и результатов тестов) по их именам.
        """
        return self.subjects.get(name, None)

    def __str__(self):
        """
        Возвращает строковое представление студента, включая имя и список предметов.
        На выходе:
        Студент: Иван Иванов
        Предметы: Математика, История
        """
        subj_str = ''
        for k, v in self.subjects.items():
            if len(v['Оценки']) != 0 or len(v['Результаты тестов']) != 0:
                subj_str += k + ', '

        if subj_str != '':
            subj_str = subj_str[:-2]

        return (f'Студент: {self.name}\n'
                # return (f'Студент: {self.__dict__['_name']}\n'
                f'Предметы: {subj_str}')

    def add_grade(self, subject, grade):
        """
        Добавляет оценку по заданному предмету.
        Убеждается, что оценка является целым числом от 2 до 5.
        Если такого предмета нет, выведите: 'Предмет {Название предмета} не найден'
        Для каждого предмета можно хранить оценки (от 2 до 5).
        В противном случае выведите:
        'Оценка должна быть целым числом от 2 до 5'
        """

        if not isinstance(grade, int) or not (2 <= grade <= 5):
            raise ValueError(f'Оценка должна быть целым числом от 2 до 5')

        if subject in self.subjects:
            self.subjects[subject]['Оценки'].append(grade)
        else:
            raise ValueError(f'Предмет {subject} не найден')

    def add_test_score(self, subject, test_score):
        """
        Добавляет результат теста по заданному предмету.
        Если такого предмета нет, выведите: 'Предмет {Название предмета} не найден'
        Убеждается, что результат теста является целым числом от 0 до 100.
         В противном случае выведите:
        'Результат теста должен быть целым числом от 0 до 100'
        """

        if not isinstance(test_score, int) or not (0 <= test_score <= 100):
            raise ValueError(f'Результат теста должен быть целым числом от 0 до 100')

        if subject in self.subjects:
            self.subjects[subject]['Результаты тестов'].append(test_score)
        else:
            raise ValueError(f'Предмет {subject} не найден')

    def get_average_test_score(self, subject) -> float:
        """
        Возвращает средний балл по тестам для заданного предмета.
        """

        if subject in self.subjects:
            if len(self.subjects[subject]['Результаты тестов']) == 0:
                return 0
            avg_tst_score = (
                    sum(self.subjects[subject]['Результаты тестов'])
                    / len(self.subjects[subject]['Результаты тестов']))
            return avg_tst_score
        else:
            raise ValueError(f'Предмет {subject} не найден')

    def get_average_grade(self) -> float:
        """
        Возвращает средний балл по всем предметам.
        """

        count = 0
        sum_grades = 0
        for subject, dicts in self.subjects.items():
            sum_grades += sum(dicts['Оценки'])
            count += len(dicts['Оценки'])
        if count == 0:
            return 0
        return sum_grades / count


if __name__ == '__main__':
    student = Student("Иван Иванов", "subjects.csv")

    student.add_grade("Математика", 4)
    student.add_test_score("Математика", 85)

    student.add_grade("История", 5)
    student.add_test_score("История", 92)

    average_grade = student.get_average_grade()
    print(f"Средний балл: {average_grade}")

    average_test_score = student.get_average_test_score("Математика")
    print(f"Средний результат по тестам по математике: {average_test_score}")

    print(student)

"""
На выходе:

Средний балл: 4.5
Средний результат по тестам по математике: 85.0
Студент: Иван Иванов
Предметы: Математика, История
"""
