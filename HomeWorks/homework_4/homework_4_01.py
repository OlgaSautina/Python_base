"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv


def calc_salary(hours_arg, rate_arg, prize_arg):
    result = hours_arg * rate_arg + prize_arg
    return result


print(argv)
hours = float(argv[1])
rate = float(argv[2])
prize = float(argv[3])
print(calc_salary(hours, rate, prize))
