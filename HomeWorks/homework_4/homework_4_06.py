"""
Реализовать два небольших скрипта:
итератор, генерирующий целые числа, начиная с указанного;
итератор, повторяющий элементы некоторого списка, определённого заранее.
Подсказка: используйте функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Предусмотрите условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3. При достижении числа 10 — завершаем цикл.
Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.
"""
from itertools import count, cycle

n = 30

# 1й скрипт - count
count_iterator = count(5)
print([next(count_iterator) for i in range(n)])

# 2й скрипт - cycle
fruits_list = ["apple", "orange", "pear", "banana"]
cycle_fruits = cycle(fruits_list)
print([next(cycle_fruits) for i in range(n)])