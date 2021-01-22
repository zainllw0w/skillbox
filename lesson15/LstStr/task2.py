word = input('Введите текст: ')
index = int(input('Номер символа: '))

list_word = list(word)
left = list_word[index - 2]
right = list_word[index]
current = list_word[index-1]

print('Слева находится: ', left)
print('Справа находится: ', right)

if left == current  and right == current:
    print('Есть два таких же символа')
elif left == current and right != current or right == current and left != current:
    print('Есть один такой символ')
else:
    print('Нет таких же символов')

