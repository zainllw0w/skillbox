sym = '@ № $ % ^ & * ( )'.split()
error = False

path = input('введите название файла: ')

for i in range(len(sym)):
    if path.startswith(sym[i]):
        print('Ошибка начинается на запрещенный символ!')
        error = True
        break
if not path.endswith('.txt') or path.endswith('.docx'):
    print('Ошибка расширения файла!')
elif error == False:
    print('Файл назван верно')

