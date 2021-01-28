text = input('Введите слово: ')
list_text = list(text)
revers_text = []
i = -1

for _ in list_text:
    revers_text.append(text[i])
    i -= 1

if list_text == revers_text:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')