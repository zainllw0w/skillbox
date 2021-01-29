zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
zoo.insert(1, 'bear')
zoo.remove('elephant')
lion = zoo.index('lion')
monkey = zoo.index('monkey')
print(zoo)
print('Лев находится на позиции: ', lion + 1)
print('Обезьяна находится на позиции: ', monkey + 1)
