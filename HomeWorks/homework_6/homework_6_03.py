class Worker:
    def __init__(self, name_p, surname_p, position_p, wage_p, bonus_p):
        self.name = name_p  # имя
        self.surname = surname_p  # фамилия
        self.position = position_p  # должность
        self._income = {"wage": wage_p, "bonus": bonus_p}  # доход - оклад и премия

    def get_full_name(self):
        result = f'{self.surname} {self.name}'
        return result

    def get_total_income(self):
        total_income = self._income["wage"] + self._income["bonus"]
        return total_income


w = Worker("Ольга", "Саутина", "Senior Big Data Scientist", 200000, 50000)
print('HR менеджер Мария: ')
print(f'- {w.get_full_name()}, добро пожаловать в нашу компанию!')
print(f'- {w.get_total_income()} р - столько вы будете получать каждый месяц на позиции {w.position}.')
print(f'{w.get_full_name()}: ')
print('- Йееехууу! Благодарю! Я готова приступить к работе.')
print('Да будет так!..')
