"""
1) Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
      который должен принимать данные (список списков) для формирования матрицы.
      Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
      Примеры матриц вы найдете в методичке.

2) Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.

3) Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, values_list):
        self.matrix = values_list

    def __str__(self):
        result = ''
        for line in self.matrix:
            for el in line:
                result += f"{el} "
            result += '\n'
        return result

    def __getitem__(self, index):
        return self.matrix[index]

    def __add__(self, other):
        size_matrix = len(self.matrix)
        i = 0
        j = 0
        result_matrix = []
        while i < size_matrix:  # по строкам
            line_matrix_1 = self.matrix[i]
            line_matrix_2 = other[i]
            j = 0
            result_line = []
            while j < size_matrix:  # по элементам в строке
                result_line.append(line_matrix_1[j] + line_matrix_2[j])
                j += 1
            result_matrix.append(result_line)
            i += 1
        return Matrix(result_matrix)


list_matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_1 = Matrix(list_matrix_1)
print(matrix_1)

list_matrix_2 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
matrix_2 = Matrix(list_matrix_2)
print(matrix_2)

matrix_3 = matrix_1 + matrix_2
print(matrix_3)
