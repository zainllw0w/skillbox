text = input('Введите строку: ')
print('Ответ: ', end='')
for i, letter in enumerate(text):
    if letter == '~':
        print(i, end=' ')