def func_ff(a, b, c):
    return a + b + c - min(a, b, c)


print(func_ff(a=float(input('Введите число ')),
              b=float(input('Введите число ')),
              c=float(input('Введите число '))))
