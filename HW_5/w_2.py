f_obj = open(input('Введите "имя".txt: '), 'w', encoding='UTF-8')
with f_obj:
    i = 0
    while True:
        text = input("Введите текст, котрый требуется записать в файл: ")
        if text == '':
            break
        j = len(text.split())
        print(f'Кол-во слов в строке {j}')
        i += 1
        f_obj.write(text + '\n')
print(f'Кол-во строк, содержащих тест: {i}')
