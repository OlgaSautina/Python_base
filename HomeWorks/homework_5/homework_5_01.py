"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
file_name = 'homework_5_01_krylov.txt'
with open(file_name, 'w', encoding="UTF-8") as f:
    print('Введите строки из вашей любимой басни Крылова:')
    while True:
        str_line = input('')
        f.writelines([str_line + "\n"])
        if str_line == '':
            break

with open(file_name, 'r', encoding="UTF-8") as f:
    print("Проверим, как записалось:")
    print(f.read())

