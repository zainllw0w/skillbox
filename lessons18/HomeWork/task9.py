text = input('Введите текст: ').split()
result = ''
module = ''
letterRev = ''

for i in range(len(text)):
    if text[i].isalpha():
        rev = text[i]
        result += ''.join(rev[::-1]) +' '
    else:
        for x in text[i]:
            if x.isalpha():
                letterRev += x
            else:
                module += letterRev[::-1] + str(x)
                letterRev = ''
        module += letterRev[::-1]
        letterRev = ''
        result += ''.join(module) +' '
        module = ''
print(result)


