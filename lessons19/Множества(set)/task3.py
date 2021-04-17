num = set()
text = input('Введите текст: ')

for i in text:
    if '0'<=i<='9':
        num.add(i)

print(num)