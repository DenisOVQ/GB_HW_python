from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, razmer):
        self.razmer = razmer

    @abstractmethod
    def raschet(self):
        pass

    @staticmethod
    def summa_tkani(args):
        k = 0
        for i in args:
            k += i
        return k


class Coat(Clothes):
    @property
    def raschet(self):
        return round(self.razmer / 6.5 + 0.5, 2)


class Suit(Clothes):
    @property
    def raschet(self):
        return round(2 * self.razmer + 0.3, 2)


a = Coat(13)
b = Suit(0.35)
print(a.raschet)
print(b.raschet)
lstr = [a.raschet, b.raschet, Coat(26).raschet, Suit(0.7).raschet, Coat(52).raschet]
print(Clothes.summa_tkani(lstr))
