class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'{self.surname} {self.name}')

    def get_total_income(self):
        print(f'Доход: {self._income.get("wage") + self._income.get("bonus")} руб.')


my_position = Position('Сергей', 'Брин', 'Водитель', 45000, 15000)
my_position.get_full_name()
my_position.get_total_income()
print(my_position.position)
