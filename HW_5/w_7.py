import json
with open("w_7.txt", 'r', encoding='UTF-8') as f_obj:
    my_list = []
    new_list = []
    for line in f_obj:
        l = (line.split()[0], int(line.split()[2]) - int(line.split()[3][:-1]))
        my_list.append(l)
    my_dict = dict(my_list)
    m, n = 0, 0
    for i in my_dict.values():
        if int(i) > 0:
            m += i
            n += 1
    my_dict["average_profit"] = m // n
    new_list.append(my_dict)
with open("w_7.json", 'w', encoding='UTF-8') as f:
    json.dump(new_list, f)
