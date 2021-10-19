def division_func(arg1, arg2):
    '''
    Делит одно первое число на второе. Предварительно проверив делитель, не является ли нулем.
    В случае, если делитель - ноль, выводит сообщение.
    :param arg1:
    :param arg2:
    :return:
    '''
    if arg2 == 0:
        print('Деление на ноль невозможно')
        return
    return arg1 / arg2


a = int(input('Введите первое число (делимое): '))
b = int(input('Введите второе число (делитель): '))
result = division_func(a, b)
print(result)
