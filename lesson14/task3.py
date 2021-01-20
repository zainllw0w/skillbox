def summ(x):
    summa = 0
    for num in str(x):
        summa += int(num)
    print('Сумма цифр в числе: ', summa)
    return summa


def countNumber(x):
    count = 0
    while x > 0:
        count += 1
        x //= 10
    print('Количество цифр в числе: ', count)
    return count


def difference(summa, count):
    print('разница суммы от количества чисел равна: ', summa, '-', count, '=', summa - count)


x = int(input('Введите число: '))


summa = summ(x)
count = countNumber(x)
difference(summa, count)
