# Опишите класс Fraction для корректной работы с дробными числами


def gdc(m, n):
    # Найти наибольший общий знаменатель
    while m % n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm % oldn
    return n


def ldc(m, n):
    # Найти наименьший общий знаменатель
    if m > n:
        greater = m
    else:
        greater = n
    while True:
        if (greater % m == 0) and (greater % n == 0):
            lcm = greater
            break
        greater += 1
    return lcm


class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return '%d/%d' % (self.num, self.den)

    def __add__(self, other):
        newnum = self.num * other.den + \
                 self.den * other.num
        newden = self.den * other.den
        common = gdc(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum

    def __le__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum <= secondnum

    def __ge__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum >= secondnum

    def __lt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum < secondnum

    def __gt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum > secondnum

    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den
        common = gdc(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __truediv__(self, other):
        newnum = self.num * other.den
        newden = self.den * other.num
        common = gdc(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __sub__(self, other):
        newden = ldc(self.den, other.den)
        mult = newden // self.den
        self.num = self.num * mult
        mult = newden // other.den
        other.num = other.num * mult
        newnum = self.num - other.num
        common = gdc(newnum, newden)

        return Fraction(newnum // common, newden // common)


test1 = Fraction(1, 2)
test2 = Fraction(2, 4)

print(test1 - test2)
print(test1 + test2)
print(test1 * test2)
print(test1 / test2)
print(test1 == test2)
print(test1 >= test2)
print(test1 <= test2)
print(test1 > test2)
print(test1 < test2)
print(test1 != test2)
