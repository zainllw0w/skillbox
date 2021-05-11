class Poteto:
    stats = {0: 'нету', 1: "росток", 2: "зеленая" ,3: "выросла"}
    def __init__(self, i):
        self.i = i
        self.state = 0

    def grow(self):
        if self.state < 2:
            self.state += 1
            self.info()
        else:
            print('Картошку можно собирать!')

    def info(self):
        print(f'{self.i} картошка, на стадии {self.stats[self.state]}')

    def isRipe(self):
        if self.state < 2:
            return False
        else:
            return True



class Garden:
    def __init__(self, count):
        self.potetos = [Poteto(i) for i in range(1, count+1)]

    def growall(self):
        print('Картошка проростает!')
        for i_poteto in self.potetos:
            i_poteto.grow()

    def check(self):
        if all([i_poteto.isRipe() for i_poteto in self.potetos]):
            print('Проросла вся!')
        else:
            print('Не проросла')


my_garden = Garden(5)
my_garden.growall()
my_garden.growall()
my_garden.growall()
my_garden.check()