text = input('Введите строку: ')
small = 0
big = 0

for i in range(len(text)):
    if text[i].islower():
        small += 1
    else:
        big += 1

print('больших букв: ', big)
print('маленьких букв: ', small)