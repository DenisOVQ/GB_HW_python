def f_func(**kwargs):
    return kwargs.values()


print(*f_func(surname=input('Фамилия '),
              name=input('Имя '),
              years_old=input('Год рождения '),
              your_city=input('Город проживания '),
              email=input('Емейл '),
              number_phone=input('Номер телефона ')))
