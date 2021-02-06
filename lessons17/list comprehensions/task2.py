text = input('Введите текст: ')
sym = input('Введите символ: ')
fist_list = [x * 2 for x in text]
second_list = [x * 2 + sym for x in text]

print(fist_list)
print(second_list)