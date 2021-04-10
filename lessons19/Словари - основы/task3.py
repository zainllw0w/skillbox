phone_book = dict()
while True:
    name = input('Введите имя: ')
    if name in phone_book:
        print('Такое имя уже есть в списке контактов!')

    number = input('Введите номер: ')
    phone_book[name] = number
    print('\nСписок контактов: ')
    for i in phone_book:
        print(i, phone_book[i])
    print()



