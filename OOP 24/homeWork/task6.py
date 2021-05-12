class Water:
    i = 1
    def __add__(self, other):
        if Water.i + other.i == 3:
            return 'Шторм'
        elif Water.i + other.i == 4:
            return "Пар"
        elif Water.i + other.i == 5:
            return 'Грязь'


class Wind:
    i = 2
    def __add__(self, other):
        if Wind.i + other.i == 5:
            return 'Молния'
        elif Wind.i + other.i == 6:
            return 'Грязь'

class Fire:
    i = 3
    def __add__(self, other):
        if Fire.i + other.i == 7:
            return 'Лава'

class Ground:
    i = 4


wat = Water()
win = Wind()
fir = Fire()
gro = Ground()

print(wat + win)
print(fir + gro)
print(win + fir)