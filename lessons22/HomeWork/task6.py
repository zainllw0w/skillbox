def func(step, text):
    my_list = [alphabet[(alphabet.index(sym) + step) % 26] if sym != ' ' else ' ' for sym in text]
    return my_list


first_time = open('text.txt', 'r')
second_time = open('cipher_text.txt', 'a')
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
              'w', 'x', 'y', 'z']
count = 1
for line in first_time:
    my_string = ''
    for letter in line:
        if letter != '\n':
            my_string += letter
    liste = func(count, my_string.lower())
    res = ''
    for i in liste:
        res += i
    second_time.write(res + '\n')
    count += 1
