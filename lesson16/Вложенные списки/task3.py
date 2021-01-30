goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]
new_fruit_list = []

new_fruit = input('Введите название нового фрукта: ')
price = int(input('Его цена: '))

new_fruit_list.append(new_fruit)
new_fruit_list.append(price)

goods.append(new_fruit_list)

print('Старые значения:', goods)

for i in range(len(goods)):
    cur_prc = goods[i][1]
    taks = (cur_prc / 100) * 8
    goods[i][1] += taks


print('С учетом процента: ', goods)