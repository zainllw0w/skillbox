sinon = dict()

n = int(input('Введите количество пар слов? '))

for i in range(1, n+1):
    print(i, 'пара: ', end='')
    text = input().lower().split(' - ')
    sinon[i] = text

print(sinon.values())


word = input('Введите слово: ')
flag = False
itog = ''

while flag == False:
    for i in sinon.values():
        if word in i:
            i.remove(word)
            itog = i
            print('Синонимы слова {0}: {1}'.format(word, itog))
            flag = True
            break
    if flag == False:
        word = input('Такого слова нет в словаре, попробуй снова: ')


