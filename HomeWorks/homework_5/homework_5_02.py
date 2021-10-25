"""
2. Создать текстовый файл (не программно),
сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""
file_name = 'homework_5_02_fedorino_gore.txt'
with open(file_name, 'r', encoding="utf-8") as f:
    n_lines = 0  # общее кол-во строк
    n_words = 0  # общее кол-во слов
    for line in f:
        n_lines += 1  # подсчитываем кол-во строк
        list_words = line.split(' ')  # разбиваем строку на слова
        n_words_line = len(list_words)
        n_words += n_words_line
        print(f'Строка {n_lines} содержит {n_words_line} слов(а)')
    print('---------------------------')
    print(f'Итого: {n_lines} строк(а), {n_words} слов(о)')

