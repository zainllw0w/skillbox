word = input('Введите слово: ')
word_list = list(word)
count = 0
unical = 0

for letter in word_list:
    for letter_2 in word_list:
        if letter == letter_2:
            count += 1
    if count < 2:
        unical += 1
        count = 0
    else:
        count = 0
print('Уникальных букв в слове: ', unical)