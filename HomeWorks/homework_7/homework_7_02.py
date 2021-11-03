"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
1) Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.

2) К типам одежды в этом проекте относятся пальто и костюм.
   У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
   Это могут быть обычные числа: V и H, соответственно.

3) Для определения расхода ткани по каждому типу одежды использовать формулы:
   - для пальто (V/6.5 + 0.5),
   - для костюма (2 * H + 0.3).

4) Проверить работу этих методов на реальных данных.

5) Реализовать общий подсчет расхода ткани.

Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


# Одежда - базовый класс
class Clothes:
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def consumption(self):
        pass


# Пальто
class Coat(Clothes):
    def __init__(self, size):
        super().__init__("Пальто")
        self.V = size

    @property
    def consumption(self):
        return round(self.V/6.5 + 0.5, 2)


# Костюм
class Suit(Clothes):
    def __init__(self, height):
        super().__init__("Костюм")
        self.H = height

    @property
    def consumption(self):
        return round(2 * self.H + 0.3, 2)


coat = Coat(10)
coat_consump = coat.consumption
print(f'Для пошива пальто понадобится {coat_consump} метров ткани')

suit = Suit(1.75)
suit_consump = suit.consumption
print(f'Для пошива костюма понадобится {suit_consump} метров ткани')

result = coat_consump + suit_consump
print(f'Для пошива пальто и костюма понадобится {result} метров ткани')
