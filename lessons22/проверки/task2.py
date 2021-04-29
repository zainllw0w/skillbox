import os
def find_file(path, file_name):
    if os.path.exists(path):
        if os.path.isfile(os.path.join(path, file_name)):
            print('Путь к файлу: {}'.format(os.path.join(path, file_name)))
            return
        else:
            for elem in os.listdir(path):
                if os.path.isdir(os.path.join(path, elem)):
                    to = os.path.join(path, elem)
                    find_file(to, file_name)



file_name = input('Введите название файла: ')
path = os.path.abspath(os.path.join('/', 'games'))
find_file(path, file_name)