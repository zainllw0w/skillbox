def func(step, text):
    my_list = [alphabet[(alphabet.index(sym) + step) % 33] if sym != ' ' else ' ' for sym in text]
    return my_list


alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

k = int(input('Введите шаг: '))
text = input('Введите текст: ').lower()

rev = func(k, text)


print('Слово которое должны зашифровать: ', text)
print('Зашифрованое слово: ', ''.join(rev) )