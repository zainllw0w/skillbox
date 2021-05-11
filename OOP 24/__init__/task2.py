class Tochka:
    x = 0
    y = 0
    count = 0
    def __init__(self, x, y):
        self.y = y
        self.x = x
        self.count += 1

    def create(self, x, y):
        self.y = y
        self.x = x
        self.count += 1


    def info(self):
        print(self.x, self.y, self.count)


t4 = Tochka(2, 5)
t2 = Tochka(1, 3)
t4.create(1, 44)
t4.info()