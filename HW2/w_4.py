a = input("Введите слова через пробел ").split(' ')
for i, j in enumerate(a):
    print(i, j[:10])
