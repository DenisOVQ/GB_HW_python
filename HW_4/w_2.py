my_list = list(map(int, input('Введите исла через пробел: ').split()))
new_list = [el for i, el in enumerate(my_list) if my_list[i] > my_list[i - 1] and i > 0]
print(new_list)
