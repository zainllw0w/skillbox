def what_is_key(name):
    for key in tree:
        for value in tree[key]:
            if name == value:
                return key


n = int(input('Введите количество человек: '))
tree = dict()


for i in range(1, n):
    print('Пара номер', i, end=': ')
    ask = input().split()
    human_list = set()
    many = set()
    for key in tree:
        for value in tree[key]:
            many.add(value)
    if ask[1] in many:
        for human in tree:
            if ask[1] in tree[human]:
                index = human
                if index + 1 in tree:
                    human_list.update(tree[index + 1])
                human_list.add(ask[0])
                tree[index + 1] = human_list
                break
    else:
        human_list.add(ask[0])
        tree[i] = human_list
        human_list = set()
        human_list.add(ask[1])
        tree[i-1] = human_list
    print(tree)

many.add(ask[0])


for i in sorted(many):
    height = what_is_key(i)
    print(i, height)