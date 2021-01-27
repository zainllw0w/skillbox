n = int(input('Введите количество моделей: '))
vd_mod = []
vd_mod_new = []
maxi = 0

for i in range(n):
    print('Введите модель', i+1, ':', end='')
    new = int(input())
    vd_mod.append(new)
    if new > maxi:
        maxi = new

for i in range(n):
    if vd_mod[i] < maxi:
        vd_mod_new.append(vd_mod[i])


print('Старые значения: ', vd_mod)
print('Новые значения: ', vd_mod_new)




