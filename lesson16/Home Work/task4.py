guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

ask = 0

while ask != 3:
    print('\nСписок гостей:', guests)
    new_guest = input('Введите имя гостя: ')
    ask = int(input('Гость пришел(1) , ушел(2), пора спать(3): '))
    if ask == 1:
        if len(guests) > 5:
            print('Прости', new_guest, 'но мест нету!')
        else:
            guests.append(new_guest)
            print('Добро пожаловать,', new_guest)
    elif ask == 2:
        guests.remove(new_guest)
        print('Пока,', new_guest)


print('Все пошли спать: ', guests)

