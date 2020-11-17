f_obj = open(input('Введите "имя".txt: '), 'w', encoding='UTF-8')
with f_obj:
    while True:
        text = input('Введите текст, котрый тербуется записать в файл: ')
        if text == '':
            break
        f_obj.write(text + '\n')
