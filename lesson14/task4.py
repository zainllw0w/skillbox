def reverse(n):
    tozp = ''
    afzp = ''
    rdyNumber = ''
    toDot = True
    afterDot = False
    for num in str(n):
        if num != '.':
            if toDot:
                tozp += num
            if afterDot and num != '.':
                afzp += num
        else:
            toDot = False
            afterDot = True
    revNum = tozp[:: -1]
    revDel = afzp[:: -1]
    rdyNumber += revNum +str('.')+ revDel
    return rdyNumber



n = float(input('Введите первое число: '))
k = float(input('Введите второе число: '))

firstNumber = reverse(n)
secondNumber = reverse(k)
summ = float(firstNumber) + float(secondNumber)

print('Сумма уже перевернутых чисел = ', firstNumber , '+', secondNumber, '= ', summ)
