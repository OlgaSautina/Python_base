"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def print_user_data(name_arg, surname_arg, year_arg, town_arg, email_arg, phone_arg):
    '''
    Выводит данные о пользователе
    :param name_arg: имя пользователя
    :param surname_arg: фамилия
    :param year_arg: год рождения
    :param town_arg: город проживания
    :param email_arg: электронная почта
    :param phone_arg: номер телефона
    :return: None. Выводит строку с указанными данными
    '''
    print(f'name: {name_arg}, '
          f'surname: {surname_arg}, '
          f'year of birth: {year_arg}, '
          f'town: {town_arg}, '
          f'email: {email_arg}, '
          f'phone number: {phone_arg}')


name = input('Input username: ')
surname = input('Input surname: ')
year = input('Input year of birth: ')
town = input('Input town: ')
email = input('Input email: ')
phone = input('Input phone: ')
print_user_data(name_arg=name, surname_arg=surname, year_arg=year, town_arg=town, email_arg=email, phone_arg=phone)
