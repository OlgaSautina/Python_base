"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа
должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyZeroDivisionError(Exception):
    def __init__(self, message):
        self._message = message

    @property
    def message(self):
        return self._message


try:
    a = int(input('Введите 1е число - делимое: '))
    b = int(input('Введите 2е число - делитель: '))
    if b == 0:
        raise MyZeroDivisionError("Делить на ноль недопустимо.")
except MyZeroDivisionError as err:
    print(err.message)
else:
    result = a / b
    print(result)
finally:
    print("Программа завершена.")
