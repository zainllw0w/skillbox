my_list = []
new_list = []
summ = 0

n = int(input('введите количество чисел в списке: '))

for _ in range (n):
    print('Введите', _ +1, 'число: ', end=' ')
    number = int(input())
    my_list.append(number)

devider = int(input('введите делитель: '))

for i in range(n):
    if my_list[i] % devider == 0:
        print('Индекс числа ', my_list[i], 'равен: ', i)
        summ += i
print('Сумма индексов равна: ', summ)