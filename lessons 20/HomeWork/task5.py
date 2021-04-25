data = {
    1: {
        ('Сидоров', 'Никита'): 22,
        ('Сидорова', 'Алина'): 20,
        ('Сидоров', 'Петр'): 2
    },
    2: {
        ('Синило', 'Виталий'): 52,
        ('Синило', 'Ирина'): 47,
        ('Синило', 'Артем'): 25
    }
}


ask = input('Введите фамилию: ').lower()

for values in data.values():
    flag = False
    for fio, age in values.items():
        if ask == fio[0].lower():
            flag = True
        if flag:
            print(f'{fio[0]}, {fio[1]} : {age}')