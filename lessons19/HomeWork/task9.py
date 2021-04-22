n = int(input('Введите количество человек: '))
tree = dict()

for i in range(1, n):
    print('Пара номер', i, end=': ')
    ask = input().split()

    if ask[1] in tree.values():
        for human in tree:
            if ask[1] in tree[human]:
                index = human
                tree[index + 1] = tree[human].append(ask[0])
    else:

        tree[i-1] = ask[1]
        tree[i] = ask[0]
print(tree)
