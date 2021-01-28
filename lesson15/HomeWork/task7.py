n = int(input('Введите количество контейнеров: '))

container = []
count = 0

for _ in range(n):
    m = int(input('Введите вес контейнера: '))
    while m > 200:
        m = int(input('Вес не должен превышать 200! Попробуйте ввести еще раз!:  '))
    container.append(m)

new_container = int(input('Введите вес нового контейнера: '))

for i in container:
    count += 1
    if new_container >= i:
        print('Позиция в которой должен быть контейнер:', count)
        break
