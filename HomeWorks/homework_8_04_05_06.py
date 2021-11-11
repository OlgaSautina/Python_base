"""
4. Начните работу над проектом «Склад оргтехники».
1) Создайте класс, описывающий склад.
2) А также класс «Оргтехника», который будет базовым для классов-наследников.
3) Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием.
   Разработать методы:
         - отвечающие за приём оргтехники на склад и
         - передачу в определенное подразделение компании.
   Для хранения данных о наименовании и количестве единиц оргтехники,
   а также других данных, можно использовать любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием.
   Реализуйте механизм валидации вводимых пользователем данных.
   Например, для указания количества принтеров, отправленных на склад,
   нельзя использовать строковый тип данных.
"""


# Склад
class Storage:
    title = ''  # название склада

    def __init__(self, title):
        Storage.title = title
        self.__equipment = {}  # словарь для хранения разных видов оргтехники

    @property
    def equipment(self):
        return self.__equipment

    # принять оргтехнику на склад
    def take_equipment(self, equipment, number_in):
        if equipment in self.__equipment.keys():
            # если такая оргтехника уже есть, то увеличиваем кол-во в словаре
            self.__equipment[equipment] += number_in
        else:
            # если такой оргтехники нет, то добавляем в словарь новую пару
            self.__equipment.update({equipment: number_in})

    # выдать оргтехнику со склада
    def give_equipment(self, equipment, number_out):
        if equipment in self.__equipment.keys():
            val = self.__equipment[equipment]
            if val >= number_out:
                # если на складе достаточно оргтехники данного вида,
                # то выдаем нужное количесто
                self.__equipment[equipment] -= number_out
            else:
                # если недостаточно, то выдаем все оставшееся кол-во
                self.__equipment[equipment] = 0

    @staticmethod
    def is_number(in_str):
        return True if in_str.isdigit() else False

    # возвращает кол-во единиц определенной оргтехники на складе
    def get_number_equipment(self, equipment):
        return self.__equipment[equipment]

    def __str__(self):
        return self.title

    def __repr__(self):
        result = ""
        for equipment, num_eq in self.__equipment.items():
            result += f'{equipment} - {num_eq} шт \n'
        return result


# Оргтехника - базовый класс
class OfficeEquipment:
    def __init__(self, name, guarantee=0, company=""):
        self.name = name  # название оргтехники
        self.guarantee = guarantee  # на сколько лет дается гарантия на данный товар
        self.company = company  # компания-производитель

    @property
    def guarantee(self):
        return self.__guarantee

    @guarantee.setter
    def guarantee(self, value):  # задается логика - можно выдавать гарантию максимум на 10 лет
        if value <= 0:
            self.__guarantee = 0
        elif value >= 10:
            self.__guarantee = 10
        else:  # от 1 до 9 лет
            self.__guarantee = value

    def __repr__(self):
        return f'{self.name} "{self.company}"'


# Принтер
class Printer(OfficeEquipment):
    def __init__(self, company_p, color, type_printer, guarantee_p):
        super().__init__("Принтер", guarantee=guarantee_p, company=company_p)
        self.color = color  # черно-белый или цветной
        self.type_printer = type_printer  # тип принтера - струйный, матричный, лазерный

    @property
    def type_printer(self):
        return self.__type_printer

    @type_printer.setter
    def type_printer(self, value):
        if value in ["струйный", "матричный", "лазерный"]:
            self.__type_printer = value
        else:
            self.__type_printer = ""
            #raise ValueError("Допустимые значения: струйный, матричный, лазерный")

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        if value in ["черно-белый", "цветной"]:
            self.__color = value
        else:
            self.__color = ""
            #raise ValueError("Допустимые значения: черно-белый, цветной")

    def __repr__(self):
        return f"{super().__repr__()} {self.color} {self.type_printer}"


# Сканер
class Scanner(OfficeEquipment):
    def __init__(self, company_s, type_scanner, guarantee_s):
        super().__init__("Сканер", guarantee=guarantee_s, company=company_s)
        self.type_scanner = type_scanner  # ручной, страничный, планшетный

    @property
    def type_scanner(self):
        return self.__type_scanner

    @type_scanner.setter
    def type_scanner(self, value):
        if value in ["ручной", "страничный", "планшетный"]:
            self.__type_scanner = value
        else:
            self.__type_scanner = ""
            #raise ValueError("Допустимые значения: ручной, страничный, планшетный")

    def __repr__(self):
        return f"{super().__repr__()} {self.type_scanner}"


# Ксерокс
class Xerox(OfficeEquipment):
    def __init__(self, company_x, type_xerox, guarantee_x):
        super().__init__("Ксерокс", guarantee=guarantee_x, company=company_x)
        self.type_xerox = type_xerox  # отдельный, МФУ, портативный

    @property
    def type_xerox(self):
        return self.__type_xerox

    @type_xerox.setter
    def type_xerox(self, value):
        if value in ["отдельный", "МФУ", "портативный"]:
            self.__type_xerox = value
        else:
            self.__type_xerox = ""
            #raise ValueError("Допустимые значения: отдельный, МФУ, портативный")

    def __repr__(self):
        return f"{super().__repr__()} {self.type_xerox}"


storage = Storage("Склад офисной техники 'Все для офиса'")
print(storage)
print('\n')

print('********************* 1 - Отправляем оргтехнику на склад *********************')
printer_1 = Printer("Samsung", "черно-белый", "матричный", 5)
printer_2 = Printer("HP", "цветной", "лазерный", 10)
printer_3 = Printer("Canon", "черно-белый", "струйный", 15)

scanner_1 = Scanner("Samsung", "ручной", 2)
scanner_2 = Scanner("Epson", "страничный", 1)
scanner_3 = Scanner("Canon", "неизвестно", 2)

xerox_1 = Xerox("Samsung", "портативный", 2)
xerox_2 = Xerox("Epson", "МФУ", 4)
xerox_3 = Xerox("Canon", "неизвестно", 15)
equipment_to = [printer_1, printer_2, printer_3, scanner_1, scanner_2, scanner_3, xerox_1, xerox_2, xerox_3]

auto = False  # Заполнять кол-во автоматически (True) или вручную (False)
number_auto = 10
for equip in equipment_to:
    print(equip)
    if auto:
        number = number_auto
        print(f'Кол-во: {number}')
    else:
        while True:
            number_str = input('Кол-во: ')
            if Storage.is_number(number_str):
                number = int(number_str)
                break
    storage.take_equipment(equip, number)

print('\n')
print('Итого на складе:')
print(storage.__repr__())

print('********************* 2 - Получаем оргтехнику со склада *********************')
# словарь (смета) - сколько техники получить со склада
give_equipment = {printer_1: 1, printer_2: 3, printer_3: 2,
                  scanner_1: 11, scanner_2: 2, scanner_3: 15,
                  xerox_1: 8, xerox_2: 9, xerox_3: 5}
for eq, value in give_equipment.items():
    print(f'На складе доступно: {eq} - {storage.get_number_equipment(eq)} шт')
    print(f'Необходимо взять: {value}')
    storage.give_equipment(eq, value)  # взять со склада
    print(f'На складе осталось: {eq} - {storage.get_number_equipment(eq)} шт')
    print('\n')

