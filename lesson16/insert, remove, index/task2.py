n = int(input('Введите количество сотрудников: '))
zp = []

for i in range(n):
    print('Введите зарплату ', i + 1, 'сотрудника: ', end='')
    salary = int(input())
    if salary != 0:
        zp.append(salary)
print('Сотрудников работающих: ', len(zp))
print('Зп: ', zp)

print('Максимальная зп: ', max(zp))
print('Минимальная зп: ', min(zp))
