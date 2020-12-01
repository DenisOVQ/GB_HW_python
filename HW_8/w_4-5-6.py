class Warehouse:
    def __init__(self):
        self._dict = {}

    def add_to(self, equipment):
        self._dict.setdefault(equipment.group_name(), []).append(equipment)

    def extract(self, name):
        if self._dict[name]:
            self._dict.setdefault(name).pop(0)

    @property
    def dict(self):
        return self._dict


class Equipment:
    def __init__(self, name, cost, year):
        self.name = name
        self.cost = cost
        self.year = year
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.name} {self.cost} {self.year}'


class Printer(Equipment):
    def __init__(self, name, cost, year, lazer):
        super().__init__(name, cost, year)
        self.lazer = lazer

    def __repr__(self):
        return f'{self.name} {self.cost} {self.year} {self.lazer}'


class Scanner(Equipment):
    def __init__(self, name, cost, year, format_a4):
        super().__init__(name, cost, year)
        self.format_a4 = format_a4

    def __repr__(self):
        return f'{self.name} {self.cost} {self.year} {self.format_a4}'


class Xerox(Equipment):
    def __init__(self, name, cost, year, colorful):
        super().__init__(name, cost, year)
        self.colorful = colorful

    def __repr__(self):
        return f'{self.name} {self.cost} {self.year} {self.colorful}'


warehouse = Warehouse()
# создаем объект и добавляем
scanner = Scanner('canon', 200, 2001, True)
warehouse.add_to(scanner)
scanner = Scanner('hp', 150, 1997, False)
warehouse.add_to(scanner)
xerox = Xerox('hp', 250, 2011, True)
warehouse.add_to(xerox)
xerox = Xerox('nicon', 200, 2014, False)
warehouse.add_to(xerox)
printer = Printer('sony', 400, 2018, True)
warehouse.add_to(printer)

# вывод оборудования на складе
print(warehouse.dict)
# забираем с склада и выводим оборудование на складе
warehouse.extract('Scanner')
warehouse.extract('Xerox')
print('\n', warehouse.dict)
