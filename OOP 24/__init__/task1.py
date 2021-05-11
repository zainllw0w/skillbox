class Toyota:
    colour = ''
    speed = 0
    maxSpeed = 200
    def __init__(self, colour, speed):
        self.speed = speed
        self.colour = colour

    def info(self):
        print(f'{self.colour}\n{self.speed}\n{self.maxSpeed}')


a1 = Toyota('green', 20)

a1.info()

