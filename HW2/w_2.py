a = list(input('Введите значения через пробел ').split(' '))
i = 0
if len(a) % 2 == 0:
    while i < len(a):
        a[i], a[i + 1] = a[i + 1], a[i]
        i += 2
    print(a)
else:
    while i < len(a) - 1:
        a[i], a[i + 1] = a[i + 1], a[i]
        i += 2
    print(a)
