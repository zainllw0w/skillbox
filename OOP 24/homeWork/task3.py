import math


def calc_interception(x1, y1, r1, x2, y2, r2):
    cen_dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return "Нет" if cen_dist > r1 + r2 else "Да"


class Rounde:
    x = 0
    y = 0
    r = 1

    def __init__(self, i):
        self.index = i

    def area(self):
        self.s = math.pi * self.r ** 2
        print(f'Площадь {self.index} равна: {self.s}')

    def perimetr(self):
        self.p = self.r * 2 * math.pi
        print(f'Периметр {self.index} равен: {self.p}')

    def enlarge(self, k):
        self.r *= k
        print(f'Радиус {self.index} увеличен и равен: {self.r}')

    def refactor(self, x, y):
        self.x = x
        self.y = y


class Graphs:
    def __init__(self, count):
        self.rounds = [Rounde(i) for i in range(1, count + 1)]

    def crossing(self):
        for current in self.rounds:
            for second in self.rounds:
                if current is not second:
                    print(f'Пересекаются ли {current.index} c {second.index}: ', end='')
                    print(calc_interception(current.x, current.y, current.r, second.x, second.y, second.r))

    def area(self, wround):
        self.rounds[wround - 1].area()

    def perimetr(self, wround):
        self.rounds[wround - 1].perimetr()

    def englarge(self, wround, k):
        self.rounds[wround - 1].enlarge(k)

    def refactor(self, wround, x, y):
        self.rounds[wround - 1].refactor(x, y)


gr1 = Graphs(2)
gr1.area(2)
gr1.refactor(2, 1, 2)
gr1.englarge(1, 2)
gr1.crossing()
