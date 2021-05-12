import random

class Unit:
    hp = 100


p1 = Unit()
p2 = Unit()
while True:
    if random.randint(1, 2) == 1:
        p2.hp -= 20
        if p2.hp == 0:
            print('p1 убил p2')
            break
        print(f'p1 ударил p2! \n p1 - {p1.hp} \n p2 - {p2.hp}')
    else:
        p1.hp -= 20
        if p1.hp == 0:
            print('p2 убил p1')
            break
        else:
            print(f'p2 ударил p1! \n p1 - {p1.hp} \n p2 - {p2.hp}')