"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(word):
    result = ''
    if len(word) > 0:
        first = word[0].upper()
        last = word[1:].lower()
        result = first + last
    return result


def int_func_sentence(sentence):
    list_words = sentence.split(' ')
    result = ''
    for w in list_words:
        w = int_func(w)
        result += ' ' + w
    return result


word_user = input('Введите любое слово: ')
print(int_func(word_user))

sentence_user = input('Введите предложение (слова, разделенные пробелом: ')
print(int_func_sentence(sentence_user))