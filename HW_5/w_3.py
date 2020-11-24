with open("my_text.txt", 'w', encoding='UTF-8') as f_obj:
    while True:
        text = input('Введите "Фамилия" "Оклад" "тыс": ')
        if text == '':
            break
        f_obj.write(text + '\n')

with open("my_text.txt", 'r', encoding='UTF-8') as f_obj_1:
    j = 0
    k = 0
    for line in f_obj_1:
        if int(line.split()[1]) < 20:
            print(line.split()[0])
        j += int(line.split()[1])
        k += 1
    print('Средняя зарплата', round(j / k, 2), 'тыс')
