def fact(n=int(input())):
    fct = 1
    for j in range(1, n + 1):
        fct *= j
        yield fct


for el in fact():
    print(el)
