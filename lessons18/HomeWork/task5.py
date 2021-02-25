def get_pas():
    global big
    big = 0
    global num
    num = 0
    global password
    password = input('Введите пароль: ')
    for p in password:
        if p.isupper():
            big += 1
        elif p == '0' or p == '1' or p == '2' or p == '3' or p == '4' or p == '5' or p == '6' or p == '7' or p == '8' or p == '9':
            num += 1

get_pas()

while len(password) < 8 or big < 1 or num < 3:
    print('Попробуйте еще раз!')
    get_pas()

print('Все введено верно!')