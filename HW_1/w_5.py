a = float(input('Введите значение выручки '))
b = float(input('Введите значение издержек '))
if a >= 0 and b >= 0:
    if a - b > 0:
        k = (a - b) / a  # чистая прибыль / выручка = рентабельность
        n = int(input('Введите кол-во сотрудников, мин. число 1 '))
        m = k / n
        print(f'Фирма работает в прибыль, рентабельность = {round(k, 2)}%',
              f'Прибыль в расчете на 1-го сотрудника {round(m, 2)}%', sep='\n')
    elif a - b == 0:
        print('Фирма работает в ноль - без прибыли')
    else:
        print('Фирма работает в минус')
else:
    print('Введите корректно значения: больше 0')
