cell = []
cell_notcurrent = []

n = int(input('Введите количество клеток: '))
for i in range(n):
    print('Эффективность', i+1, 'клетки: ', end='')
    effect = int(input())
    cell.append(effect)
    if cell[i] < i:
        cell_notcurrent.append(cell[i])
print('Неподходящие значения:')
print(cell_notcurrent)

