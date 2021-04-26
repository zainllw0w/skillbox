def  f(qe, ask='Точно?', pop=4):
    while pop > 0:
        x = input(qe)
        if x == 'da':
            y = input(ask)
            if y == 'da':
                return 1
            else:
                return 0
        else:
            pop -= 1
            print(f'осталось попыток: {pop}')

f('вы хотите удалить?', pop=2)
