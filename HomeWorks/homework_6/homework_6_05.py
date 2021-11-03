# Канцелярская принадлежность
class Stationery:
    def __init__(self, title_p):
        self.title = title_p

    def draw(self):
        return f'{self.title} -> запуск отрисовки'


# Pen (ручка), Pencil (карандаш), Handle (маркер);
class Pen(Stationery):
    def draw(self):
        return f'{self.title} -> пишем сочинение'


class Pencil(Stationery):
    def draw(self):
        return f'{self.title} -> рисуем скетч'


class Handle(Stationery):
    def draw(self):
        return f'{self.title} -> раскрашиваем картинку'


pen = Pen("Ручка Waterman")
print(pen.draw())

pencil = Pencil("Карандаш Shenzhen Toys and Craft")
print(pencil.draw())

handle = Handle("Маркер красного цвета")
print(handle.draw())