import random

class Card:
    def __init__(self):
        numb = random.randint(1,14)
        if numb < 10:
            self.bal = numb
        elif numb >= 10 and numb < 13:
            self.bal = 10
        else:
            self.bal = 11


class Game:
    cards = [Card() for _ in range(2)]
    comp = [Card() for _ in range(2)]

    score = 0
    compscore = 0
    def add(self):
        self.cards.append(Card())

    def bal(self):
        for i in self.cards:
            self.score += i.bal
        print(f'Очков: {self.score}')

    def end(self):
        for i in self.comp:
            self.compscore += i.bal
        print(f'У компа: {self.compscore} У игрока: {self.score}')
        if self.score > 21:
            print('LOSE!')
        elif self.score > self.compscore:
            print('Ты выграл')
        elif self.score == self.compscore:
            print('Ничья')
        else:
            print("Комп выграл")


gm = Game()
while True:
    ask = input('1-add<>2-show<>3-end: ')
    if ask == '1':
        gm.add()
    elif ask == '2':
        gm.bal()
    else:
        gm.end()
        break
