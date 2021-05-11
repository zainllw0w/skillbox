text = input('Введите текст: ')

try:
    file = open('res.txt', 'w')
    file.write(text)
except:
    print('Возможна ошибка!')
else:
    print('Успешно записано!')
finally:
    file.close()