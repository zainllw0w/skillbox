def is_prime(string):
    n = len(string)
    numbers = list()
    for i in range(1, n+1):
        flag = True
        for x in range(2, i):
            if i % x == 0:
                flag = False
        if flag:
            numbers.append(i)
    return numbers


def func(string):
    return [string[i] for i in is_prime(string)]

text = input('Введите текст: ').split()



print(func(text))
print(is_prime(text))
