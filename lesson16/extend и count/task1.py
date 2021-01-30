def addlist(the_list):
    main.extend(the_list)


main = [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1]
first_company = [0, 0, 0]
second_company = [1, 0, 0, 1, 1]
third_company = [1, 1, 1, 0, 1]

addlist(first_company)
addlist(second_company)
addlist(third_company)

print('Итог полученого мейн списка: ', main)
print('Количество ошибок: ', main.count(0))
