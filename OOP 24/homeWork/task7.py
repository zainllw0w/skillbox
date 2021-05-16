import random
class House:
    money = 0
    food = 50


class Human:
    hs = House()
    satiety = 50
    life = True
    if satiety == 0:
        life = False
    def __init__(self, name):
        self.name = name

    def eat(self):
        self.satiety += 10
        self.hs.food -= 10
        print('Кушает')

    def job(self):
        self.hs.money += 20
        self.satiety -= 10
        print('Пошел на работу')

    def buy(self):
        self.hs.money -= 10
        self.hs.food += 10
        self.satiety -= 5
        print('Пошел в магазин')

    def play(self):
        self.satiety -= 10
        print('Играет')



chel = Human('Incognito')

for i in range(100):
    dice = random.randint(1,6)
    print(f'Выпал кубик {dice}')
    if dice == 1:
        chel.job()
    elif dice == 2:
        chel.eat()
    elif chel.satiety < 20:
        chel.eat()
    elif chel.hs.food < 10:
        chel.buy()
    elif chel.hs.money < 50:
        chel.job()
    elif chel.life == False:
        print('Человек умер')
        break
    else:
        chel.play()
