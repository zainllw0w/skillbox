a = int(input('Введите начало диапазона: '))
b = int(input('Введите конец диапазона: '))

my_list = [x for x in range(a, b) if x % 2 == 0]

print(my_list)