from functools import reduce


def my_funcky(el_p, el_t):
    return el_p * el_t


print(reduce(my_funcky, [i for i in range(100, 1001, 2)]))
