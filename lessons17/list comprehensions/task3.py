def get_price(x , p):
    return round(x * (1 + p / 100), 2)

price = [float(input('Введите цену товара: ')) for _ in range(5)]

first_present = int(input('Введите процент на первый год: '))
second_present = int(input('Введите процент на второй год: '))

price_first = [get_price(x, first_present) for x in price]
price_second = [get_price(x, second_present) for x in price_first]

print('Сумма цен за 1й год', round(sum(price_first), 2))
print('Сумма цен за 2й год', round(sum(price_second), 2))

