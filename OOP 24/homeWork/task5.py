class Poteto:
    stats = {0: 'нету', 1: "росток", 2: "зеленая" ,3: "выросла"}
    def __init__(self, i):
        self.i = i
        self.state = 1

    def grow(self):
        if self.state < 3:
            self.state += 1
            self.info()
        else:
            print('Картошку можно собирать!')

    def info(self):
        print(f'{self.i} картошка, на стадии {self.stats[self.state]}')

    def isRipe(self):
        if self.state < 3:
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
            return True
        else:
            return False



class User:
    def __init__(self, count):
        self.gardens = [Garden(count)]

    def harvest(self):
        if self.gardens[0].check():
            print('Собираем картошку!')
            for i in self.gardens[0].potetos:
                i.state = 0
        else:
            print('Не проросла еще, нужно полить')

    def pour(self):
        if self.gardens[0].check():
            print('Картошку можно собрать, и не требует полива!')
        else:
            self.gardens[0].growall()

    def info(self):
        print(f'Сдадия грядки этого садовника: \n')
        for i in self.gardens[0].potetos:
            i.info()



p1 = User(5)
p1.info()
p1.harvest()
p1.pour()
p1.harvest()
p1.pour()
p1.harvest()
p1.info()