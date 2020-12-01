class My_Error(Exception):
    def __init__(self, text):
        self.text = text

    @staticmethod
    def my_func(number):
        my_list = []
        i = 0
        while number != 'stop':
            try:
                if number.isdigit():
                    my_list.append(number)
                else:
                    raise My_Error('Это не число')
            except My_Error as mr:
                print(mr)
            i += 1
            number = input('Введите следующий элемент: ')
        return my_list


a = My_Error.my_func(input())
print(a)
