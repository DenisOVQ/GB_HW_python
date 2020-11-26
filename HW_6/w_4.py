class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Машина {self.name}, цвета {self.color} поехла'

    def show_speed(self):
        return f'Текущая скорость: {self.speed}, Машина {self.name}, , цвета {self.color}'

    def stop(self):
        return f'Машина {self.name}, цвета {self.color} остановилась'

    def turn(self, direction):
        return f'Машина {self.name}, цвета {self.color} повернула {direction}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Скорость автомобиля {self.name} превышена на: {self.speed - 60}'
        else:
            return f'Текущая скорость автомобиля {self.name}: {self.speed}'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Скорость автомобиля {self.name} превышена на: {self.speed - 40}'
        else:
            return f'Текущая скорость автомобиля {self.name}: {self.speed}'


class PoliceCar(Car):
    def policia(self):
        if self.is_police:
            return f'Это автомобиль полиции, {self.name}, цвет {self.color}'
        else:
            return f'Это не полиция'


a = TownCar(70, 'black', 'audi', False)
b = SportCar(80, 'red', 'ferrari', False)
c = WorkCar(20, 'green', 'reno', False)
d = PoliceCar(40, 'white', 'toyota', True)
print(a.go(), a.show_speed(), a.stop(), a.turn('на север'), sep="\n")
print('\n', b.go(), b.show_speed(), b.stop(), b.turn('на юг'), sep="\n")
print('\n', c.go(), c.show_speed(), c.stop(), c.turn('на запад'), sep="\n")
print('\n', d.go(), d.show_speed(), d.stop(), d.turn('на восток'), d.policia(), sep="\n")
