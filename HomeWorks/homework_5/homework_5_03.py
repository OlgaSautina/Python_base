"""
Создать текстовый файл (не программно).
Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
Выполнить подсчёт средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""

dict_workers = dict()

# Считываем данные из файла и организуем словарь в формате Фамилия:Оклад
file_name = 'homework_5_03_workers.txt'
with open(file_name, 'r', encoding='UTF-8') as f:
    for line in f:
        list_words = line.split(' ')
        if len(list_words) < 2:
            break
        surname = list_words[0]
        salary = float(list_words[1])
        dict_workers.update({surname: salary})


# Для проверки выводим получившийся словарь
print(f'Сотрудники: {dict_workers}')

# Поиск сотрудников с окладом менее 20000р
min_salary = 20000
print(f'Сотрудники, имеющие зарплату менее {min_salary}р:')
for key, value in dict_workers.items():
    if value < min_salary:
        print(f'{key}')

# Подсчет среднего дохода всех сотрудников
sum_salary = sum(dict_workers.values())
num_workers = len(dict_workers.values())
agr_salary = round(sum_salary / num_workers, 2)
print(f'Средняя величина дохода всех сотрудников: {agr_salary}')