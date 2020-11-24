with open("w_6.txt", 'r', encoding='UTF-8') as f:
    p = []
    for line in f:
        a = line.split(':')
        b = ''.join(a[1:]).split()
        k = []
        for i in b:
            m = i.split('(')[0]
            if m.isdigit():
                k.append(m)
            l = [a[0], sum(map(int, k))]
        p.append(l)
        my_dict = dict(p)
    print(my_dict)
