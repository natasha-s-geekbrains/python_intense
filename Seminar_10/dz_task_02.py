"""На вход программе подаются два списка, каждый из которых содержит 10 различных целых чисел.
Первый список ваш лотерейный билет.
Второй список содержит список чисел, которые выпали в лотерею.
Вам необходимо определить и вывести количество совпадающих чисел в этих двух списках.

Напишите класс LotteryGame, который будет иметь метод compare_lists.
Метод будет сравнивать числа из вашего билета из list1 со списком выпавших чисел list2

Если совпадающих чисел нет, то выведите на экран:
Совпадающих чисел нет.

Пример входных данных:
list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]

game = LotteryGame(list1, list2)
matching_numbers = game.compare_lists()

Пример выходных данных:
Совпадающие числа: [3, 12, 8, 41, 9, 14, 5]
Количество совпадающих чисел: 7
"""


class LotteryGame:
    def __init__(self, lst1: [], lst2: []):
        self.list1 = lst1
        self.list2 = lst2

    @staticmethod
    def compare_lists():
        matching_nums = []
        for i in list1:
            if i in list2:
                matching_nums.append(i)
        if matching_nums:
            print(f'Совпадающие числа: {matching_nums}\n'
                  f'Количество совпадающих чисел: {len(matching_nums)}')
        else:
            print(f'Совпадающих чисел нет.')
        return matching_nums


list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]

game = LotteryGame(list1, list2)
matching_numbers = game.compare_lists()
