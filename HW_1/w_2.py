a = input('Enter seconds = ')
try:
    a = int(a)
    if a < 0:
        print('Please Enter integer positive number')
    else:
        b = a // 3600 % 24
        c = (a % 3600) // 60
        d = a % 60
        b1 = b // 10
        b2 = b % 10
        c1 = c // 10
        c2 = c % 10
        d1 = d // 10
        d2 = d % 10
        result = f"{b1}{b2}:{c1}{c2}:{d1}{d2}"
        print(result)
except ValueError:
    print('Please Enter integer positive number')
