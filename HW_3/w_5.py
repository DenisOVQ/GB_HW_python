def my_fff():
    sumka = 0
    stopper = True
    while stopper:
        numbers = input('Введите числа через пробел, "!" - стоп символ: ').split()
        x = 0
        for i in numbers:
            if i == '!':
                stopper = False
                break
            x += float(i)
        sumka += x
        if stopper:
            print(f'Текущая сумма равна: {sumka}')
        else:
            return f'Конечная сумма равна: {sumka}'


print(my_fff())
