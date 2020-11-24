my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
l = []
with open("w_4.txt", 'r', encoding='UTF-8') as f_obj:
    for line in f_obj:
        i = line.split(' - ')
        if i[0] in my_dict:
            schet = my_dict[i[0]]
        l.append((schet + ' - ' + i[1]))

with open("w_4_1.txt", 'w', encoding='UTF-8') as f_obj_1:
    f_obj_1.writelines(l)
