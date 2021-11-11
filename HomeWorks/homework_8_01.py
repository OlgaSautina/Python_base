"""
1) Реализовать класс «Дата», функция-конструктор которого
   должна принимать дату в виде строки формата «день-месяц-год».

2) В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
   Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».

3) Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
  (например, месяц — от 1 до 12).

4) Проверить работу полученной структуры на реальных данных.
"""


class Date:
    value_str = ""
    year = 0
    month = 0
    day = 0

    def __init__(self, date_str):
        Date.value_str = date_str

    @classmethod
    def to_numbers(cls):
        data_list = cls.value_str.split('-')
        cls.day = int(data_list[0])
        cls.month = int(data_list[1])
        cls.year = int(data_list[2])

    @staticmethod
    def validate_date(day, month, year):
        # сразу отсекаем отрицательные значения и 0
        if day < 1 or month < 1 or year < 1:
            return "Дата некорректна: день, месяц и год всегда больше 1"

        # Словарь - количество дней в месяце (невисокосный год)
        month_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 60, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

        # если месяц выходит из диапазона 1-12
        if month not in month_days.keys():
            return "Дата некорректна: месяц может быть только от 1 до 12"
        else:  # проверяем кол-во дней в указанном месяце
            days_val = month_days[month]
            # Делаем корректировку значения, если год високосный и указан месяц февраль (29 дней)
            if year % 4 == 0 and month == 2:
                days_val = 29
            if day > days_val:
                return f"Дата некорректна: в месяце {month} - {days_val} дней"

        return "Дата корректна"


dates_list = ["01-10-2010", "29-02-2012", "28-02-2011", "30-02-2012", "32-05-2017", "05-17-2001", "00-02-2012"]
for date_str in dates_list:
    print(f'{date_str}: ')

    # создаем объект
    date_1 = Date(date_str)

    # преобразуем в числа
    Date.to_numbers()
    print("День: ", Date.day)
    print("Месяц: ", Date.month)
    print("Год: ", Date.year)

    # вызываем метод проверки и выводим результат
    result = Date.validate_date(Date.day, Date.month, Date.year)
    print(result)
    print('\n')

