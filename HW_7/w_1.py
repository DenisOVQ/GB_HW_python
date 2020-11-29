class Matrix:
    new_list = []

    def __init__(self, my_list):
        self.my_list = my_list
        self.k = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.k < len(self.my_list):
            self.k += 1
            return self.my_list[self.k - 1]
        else:
            raise StopIteration

    def __add__(self, other):
        for i, j in zip(self.my_list, other):
            gen_lst = [x + y for x, y in zip(i, j)]
            self.new_list.append(gen_lst)
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.new_list]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.my_list]))


m_1 = Matrix([[1, 2, 3], [3, 2, 1], [1, 2, 3], [3, 2, 1]])
m_2 = Matrix([[3, 2, 1], [1, 2, 3], [3, 2, 1], [1, 2, 3]])
print(m_1, '\n')
print(m_2, '\n')
print(m_1 + m_2)
