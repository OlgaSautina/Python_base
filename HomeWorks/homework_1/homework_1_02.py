'''
Задание 2
Пользователь вводит время в секундах.
Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
'''
seconds = 0
minutes = 0
hours = 0
days = 0

seconds_user = int(input('Введите время в секундах: '))
minutes_user = seconds_user // 60
seconds = seconds_user % 60

if minutes_user >= 60:  # минут больше 60 - значит, указано время больше 1 часа, нужно высчитать часы
    hours_user = minutes_user // 60
    minutes = minutes_user % 60
    if hours_user >= 24:  # часов больше 24 - значит, указано время больше 1 суток, нужно высчитать кол-во суток
        days = hours_user // 24
        hours = hours_user % 24
else: # введено время меньше 1 часа
    minutes = minutes_user
    seconds = seconds_user % 60

if days > 0:
    print(f'{days} дн {hours:02}:{minutes:02}:{seconds:02}')
else:
    print(f'{hours:02}:{minutes:02}:{seconds:02}')

# для проверки правильности работы алгоритма, посчитаем обратно в секунды и сравним
result = days * 24 * 60 * 60 + hours * 60 * 60 + minutes * 60 + seconds
if seconds_user == result:
    print('Алгоритм работает корректно. Поздравляем, из вас выйдет хороший программист!')
else:
    print('Что-то не сходится... Проверьте алгоритм.')

