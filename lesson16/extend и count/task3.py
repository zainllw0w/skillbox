packs = []
decode = []
bad_packs = 0

n = int(input('Введите количество пакетов: '))

for i in range(n):
    print('\nВведите пакет', i+1)
    for bit in range(4):
        print('Введите', bit+1, 'бит: ', end='')
        the_bit = int(input())
        packs.append(the_bit)
    if packs.count(-1) > 1:
        bad_packs += 1
    else:
        decode.extend(packs)
    packs = []

print('Сообщение на декодировку: ', decode)
print('Клличество битых битов: ', decode.count(-1))
print('Потеряных пакетов: ', bad_packs)