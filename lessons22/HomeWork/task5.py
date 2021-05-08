import os
filePath = input('Введите путь через пробел: ').split()

stringPath = os.path.abspath(os.path.join('/'))
for i in filePath:
    stringPath = os.path.join(stringPath, i)

text = input('Введите текст!: ')

nameFile = input('Введите название файла: ')
stringPath = os.path.join(stringPath, nameFile)

if os.path.exists(stringPath):
    print('Такой файл есть хотите ли вы переписать?: ')
else:
    file = open(stringPath, 'w', encoding='utf-8')
    file.write(text)
    print('Файл сохранен!')

