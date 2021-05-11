import random

class Toyota:
    color = 'Red'
    speed = 0
    maxSpeed = 200
    price = 3000


car1 = Toyota()
car1.speed = random.randint(1, 200)
car2 = Toyota.speed


print(car1.speed)
print(car2)