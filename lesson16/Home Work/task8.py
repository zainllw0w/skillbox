user = []
i = 0
s = True
b = 0

n = int(input('Введите количество человек: '))
k = int(input('Введите число считалки: '))

user.extend(list(range(1, n + 1)))
start = user[0]

while len(user) > 1:
    for u in range(len(user)):
        if s:
            start = user[u - b]
            if start == user[-1]:
                start = user[0]
            s = False
        i += 1
        if i == k:
            print('\nСписок:', user)
            print('Отсчет начинается с:', start)
            print('Отсекается:', user[u])
            user.remove(user[u])
            s = True
            b = 1
            i = 0

print('\nВ итоге остается: ', user[0])







