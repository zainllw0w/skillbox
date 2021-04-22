import random

n = int(input('Введите максимальное число: '))

number = set()
number_user = set()
rand = random.randint(1, n)
number.add(rand)

print(number)

while True:
    ask = input('Нужное число есть среди вот этих чисел: ').split()
    if ask[0] == 'Помогите!':
        number_user.update(number)
        for i in range(2):
            number_user.add(random.randint(1, n))
        print('Артём мог загадать следующие числа: {0}'.format(number_user))
        number_user.clear()
    elif int(ask[0]) == rand:
        print('Вы угадали!')
        break
    else:
        for i in ask:
            number_user.add(int(i))

        print(number_user)

        if number_user.intersection(number):
            print('Да!')
            number_user.clear()
        else:
            print("Нет!")
            number_user.clear()