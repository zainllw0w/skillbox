employee = []

count_s = int(input('введите количество сотрудников: '))
for _ in range(count_s):
    id = int(input('Введите ID стотрудника: '))
    employee.append(id)
how = int(input('какого сотрудника ищем?'))
for eml in employee:
    if eml == how:
        flag = True
        break
    else:
        flag = False
if flag:
    print('Сотрудник на работе')
else:
    print('Сотрудник не на работе')