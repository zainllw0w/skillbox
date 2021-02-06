my_list = []
new_list = []
sequence = ''
n = int(input('Введите количество чисел: '))

for _ in range(n):
    num = int(input('Число: '))
    my_list.append(num)
    sequence += str(num)

print('\nПоследовательность: ', sequence)

for a in range(len(my_list)):
    for b in range(a, len(my_list)):
        new_list.append(my_list[b])
    if new_list[::-1] == new_list:
        new_list = []
        for c in range(a):
            new_list.append(my_list[c])
        new_list.reverse()
        break
    new_list = []
print('Нужно добавить ', len(new_list), 'чисел')
print('Сами числа: ', end='')
for i in new_list:
    print(i, end='')

