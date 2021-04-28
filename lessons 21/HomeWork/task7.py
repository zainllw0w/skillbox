def f(*args):
    summ = 0
    for i in args:
        if isinstance(i, list):
            for s in i:
                summ += f(s)
        elif isinstance(i, tuple):
                for s in i:
                    summ += s
        else:
            summ += i

    return summ


a = [[1, 2, [3]], [1], 3]
b = (1, 2, 3, 4, 5)

print(f([[1, 2, [3]], [1], 3]))

