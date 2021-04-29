import os
def finder(path):
    if os.path.exists(path):
        if os.path.isdir(path):
            print('Это папка!')
        elif os.path.isfile(path):
            print('это файл!')
            size = os.path.getsize(path)
            print(f'размер файла: {size}')
    else:
        print('Указаного пути не существует!')


path = os.path.abspath(os.path.join('/', 'games', 'steam', 'steam.exe'))

finder(path)