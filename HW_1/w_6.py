a = float(input())
b = float(input())
c = 10
i = 1
k = a
while k < b:
    k += k * 0.1
    i += 1
print(f'на {i} день достигнет результата')
