import os


def f(file, file_count = 0, size = 0):
    dir_count = 0
    for i in os.listdir(file):
        path = os.path.join(file, i)
        if os.path.isdir(path):
            dir_count += 1
            z, file_count, size = f(path, file_count, size)
        elif os.path.isfile(path):
            file_count += 1
            size += os.path.getsize(path)
    return dir_count, file_count, size

search_file = os.path.join('..')
print(search_file)

dirr, ffile, size = f(search_file)

print(f'Количество папок: {dirr}\nКоличество файлов: {ffile}\nРазмер (кб): {size/1024}')