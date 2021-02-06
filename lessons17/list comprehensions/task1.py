a = int(input('Введите начало диапазона: '))
b = int(input('Введите конец диапазона: '))

first_list = [x**3 for x in range(a, b)]
second_list = [x**2 for x in range(a, b)]

print(first_list)
print(second_list)