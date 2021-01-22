word = input('Введите строку: ')

list_word = list(word)
index = 0

for i in list_word:
    if i == ':':
        list_word[index] = ';'
    index += 1

print('Поменяные слова: ', end='')

for letter in list_word:
    print(letter, end='')

