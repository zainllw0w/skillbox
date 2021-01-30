n = int(input('Количество участников: '))
k = int(input('Количество человек в команде: '))

commands = []
num = 1
if n % k == 0:
    for i in range(n // k):
        commands.append(list(range(num, num + k)))
        num += k
    print(commands)
else:
    print(n, 'Учаснивок невозможно поделить на', k, 'команд')
