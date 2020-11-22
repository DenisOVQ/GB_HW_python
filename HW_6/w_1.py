from time import sleep
from itertools import cycle


class TrafficLight:
    __color = {'Красный': 7, 'Желтый': 2, 'Зеленый': 4}

    def running(self, counter):
        self.counter = counter
        # for i, j in self.__color.items():
        #     print(f'Горит {i} сигнал светофора')
        #     sleep(j)
        for i, j in cycle(self.__color.items()):
            if counter == 0:
                break
            print(f'Горит {i} сигнал светофора')
            sleep(j)
            counter -= 1


traf_l = TrafficLight()
traf_l.running(4)  # Кол-во режимов переключения
