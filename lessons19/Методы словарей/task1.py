def funcFind(string):
    if string in big_storage:
        print('товара', string, 'в наличии: ', big_storage.get(string))
    else:
        print('Такого товара нет в наличии!')

small_storage = {
    'гвозди': 5000,
    'шурупы': 3040,
    'саморезы': 2000
}

big_storage = {
    'доски': 1000,
    'балки': 150,
    'рейки': 600
}

big_storage.update(small_storage)

answer = input('Введите товар который вы хотите найти: ').lower()

funcFind(answer)