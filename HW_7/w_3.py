class Cage:
    def __init__(self, cell: int):
        self.cell = cell

    def __add__(self, other):
        return Cage(self.cell + other.cell)

    def __sub__(self, other):
        return Cage(self.cell - other.cell)

    def __mul__(self, other):
        return Cage(self.cell * other.cell)

    def __truediv__(self, other):
        return Cage(round(self.cell / other.cell))

    def make_order(self, row):
        base = self.cell // row
        residue = self.cell % row
        return str('\n'.join(['*' * row] * base + ['*' * residue]))

    def __str__(self):
        return f'Клетка  из количества ячеек: {self.cell}'


c1 = Cage(25)
c2 = Cage(8)
m1 = c1 + c2
m2 = c1 - c2
m3 = c1 * c2
m4 = c1 / c2
print(m1.make_order(8), '\n')
print(m2.make_order(4), '\n')
print(m3.make_order(35), '\n')
print(m4.make_order(2))
