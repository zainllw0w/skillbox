def funcCountLetter(string):
    letter = dict()
    for i in string:
        if i in letter:
            letter[i] += 1
        else:
            letter[i] = 1
    return letter

text = input('Введите текст: ').lower()

hist = funcCountLetter(text)

for i in sorted(hist.keys()):
    print(i, '=', hist[i])

print('Максимальная частота: {0}'.format(max(hist.values())))