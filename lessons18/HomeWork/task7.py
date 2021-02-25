ip = input('Введите ip адресс: ').split('.')
print(ip)
error = False

for i in range(len(ip)):
    if ip[i].isdigit():
        if int(ip[i]) < 0 or int(ip[i]) > 255:
            print('Не верное значение, цифры должны быть в диапазоне от 0 до 255')
            print('Ошибка в значении', ip[i])
            error = True
    else:
        print('Буквы не могут быть в ip адрессе!')
        error = True
if error == False:
    print('Все введено верно!')