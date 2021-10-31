"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
"""
# Создаем файл и записываем в него числа через пробел
file_name = "homework_5_05_numbers.txt"
with open(file_name, 'w', encoding="UTF-8") as f:
    print('Введите числа через пробел. Для окончания введите s.')
    while True:
        a = input('')
        if a == 's':
            break
        n = float(a)
        f.write(f'{n} ')

list_numbers = list()
with open(file_name, 'r', encoding="UTF-8") as f:
    content = f.read()
    list_numbers = content.split(' ')

sum_el = 0
for str_el in list_numbers:
    if str_el == '':
        continue
    a = float(str_el)
    sum_el += a

print(f'Сумма введенных чисел: {sum_el}')