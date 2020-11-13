def func_1(x, y):
    return x ** y


def func_2(x, y):
    k = 1
    while y != 0:
        k *= 1 / x
        y += 1
    return k


x = float(input('Введите число '))
y = int(input('Введите степень '))
print(func_1(x, y), func_2(x, y))
