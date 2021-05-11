class Toyota:
    colour = 'Red'
    money = 1000000
    speed = 0
    maxSpeed = 200

    def info(self):
        print(f'Цвет машины: {self.colour}\nСтоимость: {self.money}\nСкорость: {self.speed}\nМаксимальная скорость: {self.maxSpeed}')

    def getSpeed(self, newSpeed):
        self.speed = newSpeed


car1 = Toyota()
car1.info()
car1.getSpeed(180)
car1.info()