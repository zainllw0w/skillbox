alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
            'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
result = ''

k = int(input('Введите шаг: '))

text = input('Введите текст: ')

my_list = []
new_list = []
my_list.extend(text)

for i in range(len(my_list)):
    letter = my_list[i]
    index = alphabet.index(letter)
    if index + k > 32:
        b = 32 - index
        index = -b - 1
    new_list.append(alphabet[index + k])

for a in new_list:
    result += a

print('Слово которое должны зашифровать: ', text)
print('Зашифрованое слово: ', result)