site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

def f(word,depth, data, i=1):
    for is_key in data:
        if word in is_key:
            return data[is_key]

    for is_key in data.values():
        if isinstance(is_key, dict):
            res = f(word, depth, is_key, i+1)
            if res and i < depth:
                return res



ask = input('Искомый ключ: ')
depth = int(input('Введите глубину: '))


if f(ask, depth, site):
    print(f(ask, depth, site))
else:
    print('Такого ключа нет в этой глубине')