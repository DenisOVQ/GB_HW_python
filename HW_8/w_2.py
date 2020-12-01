class My_Error(Exception):
    def __init__(self, text):
        self.text = text


try:
    a = float(input())
    b = float(input())
    if not b:
        raise My_Error('Деление на 0')
except My_Error as mr:
    print(mr)
except ValueError as er:
    print(f'Ошибка ввода: {er}')
else:
    print(a / b)
