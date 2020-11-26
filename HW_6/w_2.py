class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass_asf(self, size):
        self.weigth = 25  # Масса асфальта 1(м2), толщиной 1(см)
        self.size = size
        k = (self._length * self._width * self.weigth * self.size) // 1000
        print(f'Масса асфальта равна: {k} тонн')


road = Road(20, 5000)  # Ширина(м), длина полотна(м)
road.mass_asf(5)  # Толщина полотна(см)
