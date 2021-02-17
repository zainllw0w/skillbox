ip_list = []
for i in range(4):
    while True:
        number = int(input('Введите число: '))
        if number > 255:
            print('Ошибка ввода данных!')
        else:
            break
    ip_list.append(number)

ip = f'{ip_list[0]}.{ip_list[1]}.{ip_list[2]}.{ip_list[3]}'

print(ip)