def ciph(text):
    count = 0
    result = ''
    letter = text[0]
    for i in range(len(text)):
        if text[i] == letter:
            count += 1
        else:
            result += letter + str(count)
            count = 1
            letter = text[i]
    result += letter + str(count)
    return result




text = input('Введите строку: ')


print(ciph(text))