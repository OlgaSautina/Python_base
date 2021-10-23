from time import sleep


class TrafficLight:
    def __init__(self):
        self.__color = "зеленый"

    def running(self):
        n = 0
        while n < 10:
            if self.__color == "красный":
                self.__color = "желтый"
                time = 2
            elif self.__color == "желтый":
                self.__color = "зеленый"
                time = 8
            elif self.__color == "зеленый":
                self.__color = "красный"
                time = 7
            else:
                self.__color = None
                time = 0
            print(f'{n+1}. Горит {self.__color} - {time} сек... ')
            sleep(time)
            n += 1


tl = TrafficLight()
tl.running()
