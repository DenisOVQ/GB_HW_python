a = int(input('Введите номер месяца от 1 до 12 '))
year = {(1, 2, 12): "Зима",
        (3, 4, 5): "Весна",
        (6, 7, 8): "Лето",
        (9, 10, 11): "Осень"}
for i in year.keys():
    if a in i:
        print('Dict: ', year.get(i))
list_year = [1, 2, 12, 3, 4, 5, 6, 7, 8, 9, 10, 11]
if a in list_year[0:3]:
    print('List: Зима')
elif a in list_year[3:6]:
    print('List: Весна')
elif a in list_year[6:9]:
    print('List: Лето')
elif a in list_year[9:]:
    print('List: Осень')
