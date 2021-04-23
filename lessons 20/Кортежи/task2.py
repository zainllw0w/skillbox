import math

def workfunc(r, h, s):
    side = 2 * math.pi * r * h
    full = side + 2 * s
    return side, full

text = input('Введите R , H,  S: ').split()


x = workfunc(int(text[0]), int(text[1]), int(text[2]))
print('side = ', x[0], 'full = ', x[1])