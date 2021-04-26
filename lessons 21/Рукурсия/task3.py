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

def find_key(data, str):
    for is_key in data:
        if str in is_key:
            return data[str]

    for is_key_m in data.values():
        if isinstance(is_key_m, dict):
            res = find_key(is_key_m, str)
            if res:
                return res
    else:
        return None


ask = input('Искомый ключ: ')

if find_key(site, ask):
    print(find_key(site, ask))
else:
    print('Такого ключа нет!')