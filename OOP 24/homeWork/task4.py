class Parent:
    children = []
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def addChild(self):
        nameChild = input('Введите имя ребенка: ')
        ageChild = input('Введите возрать ребенка: ')
        self.children.append(Children(nameChild, ageChild))

    def feed(self, name):
        for i in self.children:
            if i.name == name:
                i.hungry = False
                break

    def calm_down(self, name):
        for i in self.children:
            if i.name == name:
                i.resting_status = True
                break

    def info(self):
        print(f'Родитель: {self.name}\n Возраст: {self.age}\nДети:', end='')
        for i in self.children:
            print(f'  Ребенок: {i.name}\n  Возраст: {i.age}\n  Состояние покоя: {i.resting_status}\n  Голод: {i.hungry}\n ______________')



class Children:
    hungry = True
    resting_status = False
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Parent('Виталий', 55)
p1.addChild()
p1.feed('Артем')
p1.info()