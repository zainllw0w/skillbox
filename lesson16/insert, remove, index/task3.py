def check_films(film, film_list):
    for f in film_list:
        if film == f:
            return True
    return False


def add():
    if check_films(you_film, my_top):
        print('Фильм уже добавлен в список топов!')
    else:
        my_top.append(you_film)
        print('Фильм добавлен в список топ.')


def pos():
    if check_films(you_film, my_top):
        print('Нельзя поместить фильм который уже находится в списке топов')
    else:
        position = int(input('На какую позицию поместить? '))
        my_top.insert(position - 1, you_film)


def delete():
    my_top.remove(you_film)
    print('Фильм удален из списка топ')


films = [
    'Крепкий орешек', 'Назад в будущее', 'Таксист',
    'Леон', 'Богемская рапсодия', 'Город грехов',
    'Мементо', 'Отступники', 'Деревня',
    'Проклятый остров', 'Начало', 'Матрица'
]

my_top = []

while True:
    print('\nВаш топ фильмов: ', my_top)
    you_film = input('Ваш фильм: ')

    if check_films(you_film, films):
        ask = input('(1)Добавить фильм в топ | (2)Поместить на выбрану позицию | (3)Удалить фильм из топа \nВвод:')
        if ask == '1':
            add()
        elif ask == '2':
            pos()
        elif ask == '3':
            delete()
        else:
            print('Ошибка ввода!')
    else:
        print('Такого фильма нет в списке')