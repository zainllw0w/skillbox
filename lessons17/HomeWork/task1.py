word = input('Введите текст: ')

result = [x for x in word if x == 'а' or x == 'у' or x == 'о' or x == 'ы' or x == 'и' or x == 'э' or x == 'я' or x == 'ю' or x == 'е']

print(result)
print('Длина: ', len(result))
