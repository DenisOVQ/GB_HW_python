class Date:
    def __init__(self, date: str):
        self.date = date

    @classmethod
    def get_number(cls, date):
        my_list = []
        k = date.split('-')
        for i in k:
            my_list.append(int(i))
        return my_list

    @staticmethod
    def valid(my_list):
        if 1 <= my_list[0] <= 31 and 1 <= my_list[1] <= 12:
            return f'Date is right'
        else:
            return f'WRRRONG'


a = Date.get_number('12-12-2000')
b = Date.get_number('0-15-2000')
print(*a)
print(Date.valid(a))
print(*b)
print(Date.valid(b))
