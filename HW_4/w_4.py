my_list = list(map(int, input('Введите числа через пробел: ').split()))
print([el for el in my_list if my_list.count(el) == 1])
