numbers = [3,7,5]

while True:

 new_number = int(input('Новое число: '))

 numbers.append(new_number)

 print ('Текущий список чисел:', numbers)

 for i in numbers:

   print(i ** 2, i ** 3, i ** 4)

 print()