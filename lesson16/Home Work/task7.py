skates = []
human = []
count = 0

n = int(input('Сколько коньков: '))

for i in range(n):
    print('Введите размер', i + 1, 'конька: ', end='')
    new = input()
    skates.append(new)

n = int(input('Сколько человек: '))

for i in range(n):
    print('Введите размер ноги', i + 1, 'человека: ', end='')
    new = input()
    human.append(new)

count_human = len(human)

for a in range(len(skates)):
    for b in range(count_human):
        if human[b] <= skates[a]:
            count += 1
            human.remove(human[b])
            count_human -= 1
            break




print('Подходящих коньков: ', count)