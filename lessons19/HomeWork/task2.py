country = dict()
n = int(input('Введите количество стран: '))

for i in range(1, n+1):
    print(i, 'страна: ', end='')
    ask = input().split()
    country[ask[0]] = ask[1::]

print(country)

city = input('Введите город: ')

# for key, value in country.items():
#     if city in value:
#         print(key)
#         break
<<<<<<< HEAD

for i in country:
    if city in country.get(i):
        print('Город', city, 'расположен в', i)
        break

=======
is_exist = True
for i in country:
    if city in country.get(i):
        print('Город', city, 'расположен в', i)
        is_exist = False
        break

if is_exist:
    print('По городу', city, 'данных нет!')

>>>>>>> 9125453 (сделано задание 2 (с 3мя вариантами вывода))
# print({i for i in country if city in country.get(i)})
