incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}
print('Начальный словарь выглядит так: \n', incomes)

total = sum(incomes.values())
print('Общий доход составляет: {0}'.format(total))

minn = min(incomes.values())
nameMin = min(incomes, key=incomes.get)
print('Минимальное значение: {0}, что есть: {1}'.format(minn, nameMin))

incomes.pop(nameMin)
print('Теперь словарь выглядит так: \n', incomes)