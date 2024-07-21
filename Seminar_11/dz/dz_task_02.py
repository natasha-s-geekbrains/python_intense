class Archive:
    _instance = None

    def __new__(cls, text, number):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
            cls._instance.text = text
            cls._instance.number = number
            cls._instance.archive_text.append(cls._instance.text)
            cls._instance.archive_number.append(cls._instance.number)
        else:
            cls._instance.text = text
            cls._instance.number = number
            cls._instance.archive_text.append(cls._instance.text)
            cls._instance.archive_number.append(cls._instance.number)

        return cls._instance

    def __init__(self, text, number):
        self.text = text
        self.number = number

    def __str__(self):
        return f'Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}'

    def __repr__(self):
        return f"Archive('{self.text}', '{self.number}')"


archive1 = Archive("Запись 1", 42)
print(archive1)
archive2 = Archive("Запись 2", 3.14)
print(archive2)
archive3 = Archive("Third Text", 3)
print(archive3)



