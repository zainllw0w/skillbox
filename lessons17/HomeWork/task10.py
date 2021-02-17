def func(step, text):
    my_list = [alphabet[(alphabet.index(sym) + step) % 33] if sym != ' ' else ' ' for sym in text]
    return my_list


alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
result = ''

k = int(input('Введите шаг: '))
text = input('Введите текст: ')

rev = func(k, text)

for i in rev:
    result += i

print('Слово которое должны зашифровать: ', text)
print('Зашифрованое слово: ', result)