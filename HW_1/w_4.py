a = int(input())
h = str(a)
i = 0
k = 0
while i < len(h):
    if k < int(h[i]):
        k = int(h[i])
    else:
        k = k
    i += 1
print(k)
