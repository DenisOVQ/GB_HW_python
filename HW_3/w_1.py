def my_func(arg_1, arg_2):
    try:
        x = arg_1 / arg_2
        return x
    except ZeroDivisionError as err1:
        return err1, 'Деление на ноль'


print(my_func(float(input('Введите делимое: ')),
              float(input('Введите делитель: '))))
