import os

file = open(os.path.join('numbers.txt'), 'r')
summ = 0

for line in file:
    summ += int(line)

file.close()

new_file = open('new_number.txt', 'w')
new_file.write(str(summ))
new_file.close()