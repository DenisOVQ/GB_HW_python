f_obj = input('Введите "имя".txt: ')
with open(f_obj, 'w', encoding='UTF-8') as f:
    while True:
        numbers = input('Введите числа через пробел: ')
        if numbers == '':
            break
        f.write(numbers + '\n')
with open(f_obj, 'r', encoding='UTF-8') as f:
    a = 0
    for line in f:
        a += sum(list(map(int, line[:-1].split())))
    print(f'сумма чисел {a}')
