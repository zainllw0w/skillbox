my_list = []
n = int(input('Введите число: '))

for a in range(1, n+1):
    if a % 2 != 0:
        my_list.append(a)
print(my_list)
