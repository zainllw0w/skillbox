import string
import random

alphabet = string.ascii_lowercase
try:
    file = open('ages.txt', 'r')
except FileNotFoundError:
    print('Такой файл небыл найден!')
except IsADirectoryError:
    print('Ожидался файл но оказалась директория!')
sttr = ''

for i in file:
    letter = random.choice(alphabet)
    try:
        i = int(i)
        sttr += f'{letter} - {i}\n'
    except ValueError:
        print('в файле есть текст!> он был удален')


file.close()
try:
    file = open('result.txt', 'w')
    file.write(sttr)
except FileExistsError:
    print('Такой файл уже создан!')

