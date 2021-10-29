"""
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти чётные числа от 100 до 1000 (включая границы).
Нужно получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce


def multiply_list_func(a, b):
    return a * b


my_list = [el for el in range(100, 1001) if el % 2 == 0]
print(my_list)

result = reduce(multiply_list_func, my_list)
print(result)
