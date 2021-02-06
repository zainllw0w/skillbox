my_list = []
sequence = ''
n = int(input('Введите количество чисел: '))

for _ in range(n):
    num = int(input('Введите число: '))
    my_list.append(num)
    sequence += str(num)

print('\nПоследовательность: ', sequence)

if my_list[-1] == my_list[-2]:
    print('Нужно дописать чисел: ', n - 2)
    for i in range(len(my_list) - 3, -1, -1):
        print('Сами числа: ', my_list[i])
else:
    print('Нужно дописать чисел: ', n - 1)
    for i in range(len(my_list) - 2, -1, -1):
        print('Сами числа: ', my_list[i], end='')

