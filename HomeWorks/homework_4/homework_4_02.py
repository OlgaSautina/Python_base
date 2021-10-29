"""
Представлен список чисел.
Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
"""


list_num = [10, 12, 53, 45, 67, 2, 4, 0, -9, 3, 52, 6]
new_list_num = [list_num[i] for i in range(0, len(list_num)) if list_num[i] > list_num[i - 1]]
print(new_list_num)
