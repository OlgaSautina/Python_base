"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен
записываться в новый текстовый файл.
"""

# Считываем данные из файла и сохраняем их в список
file_name_eng = "homework_5_04_numbers_eng.txt"
lines_list = list()
with open(file_name_eng, 'r', encoding="UTF-8") as f:
    lines_list = f.readlines()

# Выводим получившийся список для проверки
print(f'Список - на английском: {lines_list}')

# Формируем словарь - перевод английских чисел на русские в формате Англ:Рус
numbers_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}


# Функция-перводчик с английского на русский
def translate(str_eng):
    """
    Переводит строку на английском в строку на русском с помощью словаря
    :param str_eng: Строка на английском языке
    :return: Строка на русском языке
    """
    result = str_eng
    for key, value in numbers_dict.items():
        if key in str_eng:
            result = str_eng.replace(key, value)
            break
    return result


# Проходимся по списку из файла и заменяем английские слова на русские
file_name_rus = "homework_5_04_numbers_rus.txt"
with open(file_name_rus, 'w', encoding="UTF-8") as f:
    for lineEng in lines_list:
        line_rus = translate(lineEng)
        # сразу записываем в новый файл
        f.write(line_rus)

# Для проверки - считываем, что получилось в новом файле
with open(file_name_rus, 'r', encoding="UTF-8") as f:
    content = f.read()
    print('Результат - на русском: ')
    print(content)
