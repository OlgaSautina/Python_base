class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_asphalt_mass(self, mass_1cm, thick_cm):
        result = self._length * self._width * mass_1cm * thick_cm
        return result


length_1 = 1000
width_1 = 5
road = Road(length_1, width_1)
mass_1 = 0.3
thick_1 = 7
mass_asphalt = road.calc_asphalt_mass(mass_1, thick_1)
print(f'Для покрытия дороги асфальтом длиной {length_1}м и шириной {width_1}м потребуется {mass_asphalt} т асфальта')
