films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
like_films = []
not_search = False
film = ''

while film != 'end':
    film = input('Введите фильм: ')

    for f in films:
        if film == f:
            like_films.append(film)
            print('Фильм добавлен в список желаемых')
            not_search = False
            break
        else:
            not_search = True
    if not_search:
        print('Нет рецензии на этот фильм!')

print('Вы можете посмотреть рецензии на фильмы: ', like_films)