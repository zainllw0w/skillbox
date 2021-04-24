def find_people(ser, numb):
    for key, value in data.items():
        if ser in key and numb in key:
            return value[1], value[0]

data = {
    (5000, 123456): ('Иванов', 'Василий'),
    (6000, 111111): ('Иванов', 'Петр'),
    (7000, 222222): ('Медведев', 'Алексей'),
    (8000, 333333): ('Алексеев', 'Георгий'),
    (9000, 444444): ('Георгиева', 'Мария')
}

ask = input('Введите серию и номер паспорта через пробел: ').split()

name, surname = find_people(int(ask[0]), int(ask[1]))


print(name, surname)
