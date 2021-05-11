class Family:
    surname = 'Bitches'
    money = 25000
    house = False

    def info(self):
        print(f'Фамилия: {self.surname}\nКоличество бабла:{self.money}\nНаличие дома: {self.house}')

    def byeHouse(self, prise):
        if self.money >= prise:
            self.money -= prise
            self.house = True
            print('Дом куплен!')
        else:
            print(f'Недостаточно средств!, не хватило: {prise - self.money}')

    def makeMoney(self, howMach):
        self.money += howMach
        print(f'Заработано {howMach} бабла')



fam = Family()
fam.info()
fam.byeHouse(30000)
fam.makeMoney(25000)
fam.byeHouse(30000)
fam.info()

