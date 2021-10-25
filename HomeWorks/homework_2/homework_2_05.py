"""
Реализовать структуру «Рейтинг»
"""
my_list = [7, 5, 3, 3, 2, 5, 8]
my_list.sort(reverse=True)
print(my_list)

a = int(input('Введите значение рейтинга: '))
if a in my_list:  # если такой же уже есть в списке
    index_a = my_list.index(a)
    my_list.insert(index_a, a)  # вставляем новый элемент рядом
else:
    # добавить в подходящее место в списке
    print("Нет такого рейтинга, попробуем добавить...")
    if a > my_list[0]:  # если больше всех, то вставляем на первое место
        my_list.insert(0, a)
    elif a < my_list[len(my_list) - 1]:
        my_list.insert(len(my_list), a)  # если меньше всех, вставляем в конец
    else:  # ищем, куда вставить в средину
        n = 1
        while n < len(my_list):
            if my_list[n - 1] > a > my_list[n]:
                my_list.insert(n, a)
                break
            n += 1

print(my_list)
