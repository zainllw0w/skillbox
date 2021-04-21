def hyst(text):
    for i in text:
        if i in sym:
            sym[i] += 1
        else:
            sym[i] = 1

def rev_hyst(sym):
    for i in sym:
        if sym[i] in rev_sym:
            rev_sym[sym[i]] = rev_sym[sym[i]] + ',' + str(i)
        else:
            rev_sym[sym[i]] = i

text = input('Введите текст: ')
sym = {}
rev_sym = {}

hyst(text)
print(sym)

rev_hyst(sym)
for i in rev_sym:
    print(i, end=': ')
    print(rev_sym[i])