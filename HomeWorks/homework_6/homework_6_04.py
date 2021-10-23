class Car:
    def __init__(self, name_p, color_p, speed_p, is_police_p):
        self.name = name_p
        self.color = color_p
        self.speed = speed_p
        self.is_police = is_police_p

    def go(self):
        return f'{self.name} едет'

    def stop(self):
        return f'{self.name} остановился(ась)'

    def turn(self, direction):
        return f'{self.name} поворачивает {direction}'

    def show_speed(self):
        return f'Текущая скорость: {self.speed} км/ч'

    def is_police_car(self):
        if self.is_police:
            return 'Да'
        else:
            return 'Нет'


class TownCar(Car):
    max_speed = 60

    def __init__(self, name_p, color_p, speed_p):
        super().__init__(name_p, color_p, speed_p, False)

    def go(self):
        return f'{self.name} проезжал(а) мимо'

    def show_speed(self):
        result = f'Текущая скорость: {self.speed} км/ч'
        if self.speed > TownCar.max_speed:
            result += 'Превышение максимально допустимой скорости!'
        return result


class SportCar(Car):
    max_speed = 60

    def __init__(self, name_p, color_p, speed_p):
        super().__init__(name_p, color_p, speed_p, False)

    def go(self):
        return f'вылетает {self.name}'

    def stop(self):
        return f'{self.name} врезается в дерево'

    def show_speed(self):
        result = f'Текущая скорость: {self.speed} км/ч. '
        if self.speed > SportCar.max_speed:
            result += 'Превышение максимально допустимой скорости!'
        return result


class WorkCar(Car):
    max_speed = 40

    def __init__(self, name_p, color_p, speed_p):
        super().__init__(name_p, color_p, speed_p, False)

    def show_speed(self):
        print(f'Текущая скорость: {self.speed} км/ч')
        if self.speed > TownCar.max_speed:
            print(f'Вы превысили максимальную скорость!')


class PoliceCar(Car):
    def __init__(self, name_p, color_p, speed_p):
        super().__init__(name_p, color_p, speed_p, True)


sport_car = SportCar("Молния Маккуин", "красного цвета", 200)
police_car = PoliceCar("Док Хадсон", "черного цвета", 20)
town_car = TownCar("Салли Каррера", "небесно-голубого цвета", 30)
work_car = WorkCar("Мэтра-эвакуатора", "ржавого цвета", 0)

print('Тихая спокойная улица в городе Радиатор-Спрингс.')
print(f'{police_car.go()} со скоростью {police_car.speed} км/ч. Полицейский!?? {police_car.is_police_car()}.')
print(f'И вдруг на бешеной скорости {sport_car.speed} км/ч {sport_car.go()}, спортивная машина {sport_car.color}.')
print(f'{police_car.name} наставляет на него радар и видит: {sport_car.show_speed()}')
print(f'{sport_car.turn("налево")}. {sport_car.turn("направо")}. В итоге {sport_car.stop()}...')
print(f'Подруга нарушителя, милая машинка {town_car.color} - {town_car.go()} и подумала: ')
print(f'- Ну вот, опять вызывать {work_car.name}, нашего любимого друга {work_car.color}.')
print(f'И с жалостью посмотрела на медленно поднимающийся дымок у дерева...')

