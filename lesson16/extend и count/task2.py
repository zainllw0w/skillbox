def visual(my_list):
    for letter in my_list:
        print(letter, end='')


text1 = input('Введите строку 1: ')
text2 = input('Введите строку 2: ')

first_list = list(text1)
second_list = list(text2)

sym1 = first_list.count('!') + first_list.count('?')
sym2 = second_list.count('!') + second_list.count('?')

if sym1 > sym2:
    first_list.extend(second_list)
    visual(first_list)
else:
    second_list.extend(first_list)
    visual(second_list)