"""
1) Создать вручную и заполнить несколькими строками текстовый файл,
   в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
   Пример строки файла: firm_1   ООО   10000   5000.
2) Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
   Если фирма получила убытки, в расчёт средней прибыли её не включать.
3) Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
   а также словарь со средней прибылью.
   Если фирма получила убытки, также добавить её в словарь (со значением убытков).
   Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
4) Итоговый список сохранить в виде json-объекта в соответствующий файл.
   Пример json-объекта:
   [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
   Подсказка: использовать менеджер контекста.
"""
import json


file_name = "homework_5_07_firms.txt"
list_total = []  # список словарей - со всеми начальными данными
with open(file_name, 'r', encoding="UTF-8") as f:
    print('1. Получили данные из файла: ')
    print(f.read())
    f.seek(0)
    print('')
    n = 0
    # считываем построчно и формируем словарь с изначальными данными
    for line in f:
        line_temp = line.replace('\n', '')
        words_list = line_temp.split(' ')
        firm_dict = {}
        firm_dict.update({"name":words_list[0]})  # название фирмы
        firm_dict.update({"form": words_list[1]})  # форма собственности
        proceeds = float(words_list[2])  # выручка
        firm_dict.update({"proceeds": proceeds})
        expenses = float(words_list[3]) # издержки
        firm_dict.update({"expenses": expenses})
        firm_dict.update({"fin_result": proceeds - expenses})  # финансовый результат - прибыль или убыток
        n += 1
        list_total.append(firm_dict)
        # Сформировали список и выходим из файла, чтобы не занимать для других процессов

print('Сформировали список словарей для дальнейшего анализа: ')
print(list_total)
print('')

print('2. Средняя прибыль: ')
total_profit = 0
n = 0
for info in list_total:
    fin_result = info.get("fin_result")
    if fin_result > 0:
        total_profit += fin_result
        n += 1

average_profit = 0
average_dict = {}
if n > 0:
    average_profit = round(total_profit / n, 2)
    average_dict.update({"average_profit": average_profit})
print(average_profit)
print('')

# формируем словарь с фирмами и прибылью\убытками
profits_dict = {}
for el in list_total:
    profits_dict.update({el.get("name"): el.get("fin_result")})

# формируем итоговый список
result_list = [profits_dict, average_dict]
print("3. Сформировали итоговый список по прибыли и убыткам:")
print(result_list)
print('')

# записываем в json-файл итоговый список
print('4. Записываем итоговый список в json-файл.')
with open("homework_5_07_firms.json", "w", encoding="UTF-8") as f:
    json.dump(result_list, f)

print('Проверим, что получилось в файле:')
with open("homework_5_07_firms.json", "r", encoding="UTF-8") as f:
    print(json.load(f))

