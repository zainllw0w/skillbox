shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100],
        ['седло', 1500], ['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]]

count = 0
money = 0

name_detail = input('Введите название детали: ')

for i in range(len(shop)):
        if shop[i][0] == name_detail:
                count += 1
                money += shop[i][1]

print('Деталь: ', name_detail, '\nКличество: ', count, '\nСтоисомть: ', money)

