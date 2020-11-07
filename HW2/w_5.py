my_list = [9, 8, 8, 7, 6, 4, 4, 3, 2]
a = int(input())
if a <= my_list[-1]:
    my_list.append(a)
else:
    for i, j in enumerate(my_list):
        if a > j:
            my_list.insert(i, a)
            break
print(my_list)
