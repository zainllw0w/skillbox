n = int(input('Сколько друзей?: '))
k = int(input('Клличество долговых расписок: '))

friends = []
my_list = []

for i in range(n):
    my_list.append(i + 1)
    my_list.append(0)
    friends.append(list(my_list))
    my_list.remove(my_list[0])
    my_list.remove(my_list[0])

for i in range(k):
    print('\n', i + 1, 'расписка')
    out = int(input('От кого: '))
    inn = int(input('Кому: '))
    price = int(input('Сколько: '))

    friends[out - 1][1] += price
    friends[inn - 1][1] += -price

for i in range(n):
    print(friends[i][0], ':', friends[i][1])