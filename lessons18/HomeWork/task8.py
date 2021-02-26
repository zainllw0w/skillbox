def calculate(text, second_text):
    k = 1
    for _ in range(len(text)):
        my_list = [text[(text.index(sym) + k) % len(text)] for sym in text]
        result = ''.join(my_list)
        if result == second_text:
            return k
        else:
            k += 1
    return False





text = 'abcd'
second_text = "cdab"


result = calculate(text, second_text)

if result > 1:
    print('Сдвигов должно быть сделано: ', result)
else:
    print('Задача не имеет рещения')







