def int_func(word):
    return word.capitalize()


print(' '.join(map(int_func, input('Введите текст: ').split())))
