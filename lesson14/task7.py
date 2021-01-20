
count = 0

start = int(input('Введите начало года: '))
end = int(input('Введите конец года: '))

for year in range(start, end + 1):
    text = '' + str(year)
    for num in str(year):
        i = 0
        while i < 4:
            if num == text[i]:
                count += 1
                i += 1
            else:
                i += 1
        if count == 3:
            print(year)
            count = 0
            break
        else:
            count = 0
