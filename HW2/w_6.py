a = int(input('Введите кол-во товаров '))
my_list = []
name_list = []
cost_list = []
kol_list = []
edin_list = []
my_tuple = ()
new_dict = {}
i = 1
while i <= a:
    name = input('Введите название товара ')
    cost = input('Введите стоимость товара ')
    kol_vo = input('Введите количество товара ')
    edin = input('Введите единица изм. товара ')
    my_dict = {"название": name,
               "цена": cost,
               "количество": kol_vo,
               "ед": edin}
    my_tuple = (i, my_dict)
    my_list.append(my_tuple)
    name_list.append(my_list[i - 1][1].get("название"))
    cost_list.append(my_list[i - 1][1].get("цена"))
    kol_list.append(my_list[i - 1][1].get("количество"))
    edin_list.append(my_list[i - 1][1].get("ед"))
    i += 1
new_dict = {"название": name_list,
            "цена": cost_list,
            "количество": kol_list,
            "ед": set(edin_list)}
print("Готовая структура", my_list, "Аналитика товара", new_dict, sep="\n")
