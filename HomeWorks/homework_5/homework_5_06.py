"""
Сформировать (не программно) текстовый файл.
В нём каждая строка должна описывать учебный предмет и наличие лекционных,
практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий.
Необязательно, чтобы для каждого предмета были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
Примеры строк файла:    Информатика: 100(л)  50(пр)  20(лаб).
                        Физика:      30(л)    —      10(лаб)
                        Физкультура:  —      30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
lesson_types_list = ['(л)', '(пр)', '(лаб)']
lesson_types_dict = {"(л)": "лекции", "(пр)": "практики", "(лаб)": "лабораторные"}


def get_dict_lessons(str_lessons):
    """
    Превращает строку в формате '100(л) 50(пр) 20(лаб)'
    в словарь в формате {"лекции": 100, "практики": 50, "лабораторные": 20}
    :param str_lessons: Строка в формате '100(л) 50(пр) 20(лаб)'
    :return: Словарь в формате {"лекции": 100, "практики": 50, "лабораторные": 20}
    """
    dict_result = {}
    # получаем список слов
    words = str_lessons.split(' ')
    word_temp = ''

    # работаем с каждым словом - разделяем численную и буквенную части
    for word in words:
        n_hours = 0
        type_founded = ''

        # определяем, какой тип занятия указан в строке
        for t in lesson_types_list:
            if t in word:
                type_founded = t

                # нашли и заменяем на пустую строку
                word_temp = word.replace(type_founded, '')

                # также удаляем лишние символы
                if '\n' in word_temp:
                    word_temp = word_temp.replace('\n', '')

                # если значение не указано, значит 0, иначе - получаем целое значение
                if word_temp == '' or word_temp == '—' or word_temp == '-':
                    n_hours = 0
                else:
                    n_hours = int(word_temp)

                # записываем в словарь, только если указано значение
                if n_hours > 0:
                    full_lesson_name = lesson_types_dict.get(type_founded)
                    dict_result.update({full_lesson_name: n_hours})
                    break  # дальше можно не искать, т.к. тип может быть указан только 1 раз
    return dict_result


# Основная часть программы
temp_dict = {}
file_name = "homework_5_06_study_plan.txt"

with open(file_name, 'r', encoding="UTF-8") as f:
    print('1. Считываем данные из файла: ')
    print(f.read())
    print('')

    # Создаем промежуточный словарь с полным описанием предметов и занятий
    f.seek(0)
    for line in f:
        # разделяем предмет и кол-во разных занятий
        words_list = line.split(':')
        name_subject = words_list[0]  # предмет
        value_lessons_dict = get_dict_lessons(words_list[1])  # разные занятия с указанием часов
        temp_dict.update({name_subject: value_lessons_dict})  # записывааем в промежуточный словарь


print('2. Переводим в промежуточный словарь, удобный для дальнейшего анализа: ')
print(temp_dict)
print('')

# Считаем кол-в часов по каждому предмету и выводим итоговый словарь
result_dict = {}
for subject, lessons in temp_dict.items():
    result_dict.update({subject: sum(lessons.values())})

print('3. Результат: ')
print(result_dict)
