def add_contact(data):
    ask = input('Введите фамилию и имя через пробел: ').split()
    for i in data:
        if ask[0] in i and ask[1] in i:
            print('Такой контакт уже есть в телефонной книжке!')
            break
    number = input('Введите номер телефона: ')
    data[tuple(ask)] = number


def found_contact(data):
    founder_user = dict()
    ask = input('Введите фамилию: ')
    for i in data:
        if ask in i:
            founder_user[i] = data[i]
    for key, value in founder_user.items():
        print(f'ФИО: {key[0]} {key[1]} номер телефона: {value}')




data = dict()

while True:
    ask = int(input('1 - добавить контакт, 2 - найти контакт: '))
    if ask == 1:
        add_contact(data)
    elif ask == 2:
        found_contact(data)
    print(f'Полный словарь: {data}')


