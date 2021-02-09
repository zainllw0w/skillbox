import random

n = 10
k = 3

skittles = ['I' for _ in range(n)]
knock = []
print(skittles)

for _ in range(k):
    l = random.randint(1, n - 1)
    r = random.randint(l, n - 1)
    for i in range(l, r + 1):
        if skittles[i] == 'I':
            knock.append(i)
            minn = min(knock)
            maxx = max(knock)
    if minn != maxx:
        print('Были cбиты кегли', minn, maxx)
    elif minn == 0:
        print('Пролетела сквозь сбитые')
    else:
        print('Была сбита одна кегля под номером: ', minn)
    knock = []
    minn = 0
    maxx = 0
    skittles[l - 1:r] = '.' * (r - l + 1)
    print(skittles)
