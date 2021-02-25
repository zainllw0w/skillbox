text = input('Введите строку: ').split()
count = 0

for i in text:
    print(i)
    if len(i) > count:
        count = len(i)
        word = i

print('Самое длинное слово: ', word, 'состоящее из ', count, 'символов')

