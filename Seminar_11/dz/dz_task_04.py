class Matrix:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def __str__(self):
        str_matrix = ''
        for i in range(self.rows):
            str_row = [str(n) for n in self.data[i]]
            str_matrix += ' '.join(str_row)
            if i in range(self.rows - 1):
                str_matrix += '\n'
        return str_matrix
    # return '\n'.join([' '.join([str(self.data[i][j]) for j in range(self.cols)]) for i in range(self.rows)])

    def __repr__(self):
        # str_matrix = ''
        # for i in range(self.rows):
        #     for j in range(self.cols):
        #         str_matrix += str(self.data[i][j])
        #         str_matrix += ' '
        #     str_matrix += '\n'
        return f'Matrix({self.rows}, {self.cols})'

    def __eq__(self, other):
        """Метод, определяющий операцию "равно" для двух матриц.
        Сравнивает две матрицы и возвращает True, если они имеют одинаковое количество строк и столбцов,
        а также все элементы равны. Иначе возвращает False."""

        count = self.rows
        if self.rows == other.rows and self.cols == other.cols:
            for i in range(self.rows):
                count -= self.data[i] == other.data[i]
            return count == 0

    def __add__(self, other):
        """Метод, определяющий операцию сложения двух матриц.
        Проверяет, что обе матрицы имеют одинаковые размеры (количество строк и столбцов).
        Если размеры совпадают, создает новую матрицу,
        где каждый элемент равен сумме соответствующих элементов входных матриц."""
        sum_matrix = Matrix(self.rows, self.cols)
        if self.rows == other.rows and self.cols == other.cols:
            for i in range(self.rows):
                for j in range(self.cols):
                    sum_matrix.data[i][j] = self.data[i][j] + other.data[i][j]
        else:
            raise ValueError("Матрицы должны иметь одинаковые размеры")
        return sum_matrix

    def __mul__(self, other):
        """Метод, определяющий операцию умножения двух матриц.
        Проверяет, что количество столбцов в первой матрице равно количеству строк во второй матрице.
        Если условие выполняется, создает новую матрицу,
        где элемент на позиции [i][j] равен сумме произведений элементов соответствующей строки
        из первой матрицы и столбца из второй матрицы."""

        mul_matrix = Matrix(self.rows, other.cols)
        if self.cols == other.rows:
            for i in range(self.rows):
                for j in range(other.cols):
                    for k in range(self.cols):
                        mul_matrix.data[i][j] += self.data[i][k] * other.data[k][j]
        else:
            raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы")
        return mul_matrix


# Создаем матрицы
matrix1 = Matrix(2, 3)
matrix1.data = [[1, 2, 3], [4, 5, 6]]
matrix2 = Matrix(2, 3)
matrix2.data = [[7, 8, 9], [10, 11, 12]]
matrix_new = Matrix(2, 3)
matrix_new.data = [[1, 2, 3], [4, 5, 6]]
# Выводим матрицы
print(matrix1)
print(matrix2)
print(matrix1 == matrix2)

# Выполняем операцию сложения матриц
matrix_sum = matrix1 + matrix2
print(matrix_sum)

# Выполняем операцию умножения матриц
matrix3 = Matrix(3, 2)
matrix3.data = [[1, 2], [3, 4], [5, 6]]

matrix4 = Matrix(2, 2)
matrix4.data = [[7, 8], [9, 10]]

result = matrix3 * matrix4
print(result)
