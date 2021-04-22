n = int(input('Введите количество заказов: '))
data = dict()

for i in range(1, n+1):
    print('Заказ', i, end=': ')
    order = input().lower().split()
    if order[0] in data:
        if order[1] in data[order[0]]:
            data[order[0]][order[1]] += int(order[2])
        else:
            data[order[0]][order[1]] = int(order[2])
    else:
        data[order[0]] = {order[1]: int(order[2])}


print()

for i in data:
    print('{0}: '.format(i))
    for x in data[i]:
        print('   {0}: {1}'.format(x, data[i][x]))

