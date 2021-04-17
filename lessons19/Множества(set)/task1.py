marks = set('.,;:!?')
text = input('Введите текст: ')
count = 0
for i in text:
    count += len(marks.intersection(i))
print(count)
