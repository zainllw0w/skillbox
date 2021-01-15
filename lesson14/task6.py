x = float(input('Х: '))
y = float(input('Y: '))
r = float(input('Введите радиус: '))

if x ** 2 + y ** 2 <= r ** 2:
    print('Монетка гдето рядом')
else:
    print('Монетки рядом нет!')
