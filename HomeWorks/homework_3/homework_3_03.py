"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(a, b, c):
    """
    Вычисляет сумму двух наибольших чисел: создает список из аргументов, сортирует его по убыванию,
    берет первые два числа из списка и складывает их
    :param a: первое число
    :param b: второе число
    :param c: третье число
    :return: сумма двух наибольших чисел
    """
    my_list = [a, b, c]
    my_list.sort(reverse=True)
    print(my_list)
    result = my_list[0] + my_list[1]
    return result


print(my_func(2, 4, -7))
