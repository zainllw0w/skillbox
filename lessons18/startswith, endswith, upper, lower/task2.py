path = 'c:/user/docs/folder/new_file.txt'.lower()
disc = input('На каком диске должен лежать файл: ').lower()
expansions = input('Каким должно быть расширение файла: ').lower()

if path.endswith(expansions) and path.startswith(disc):
    print('Путь коректен!')
else:
    print('Ощибка!')