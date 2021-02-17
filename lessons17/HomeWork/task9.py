def func(a,b,c):
    if c >= 3 and c < 6:
        b += 1
        c -= 3
    if c >= 6 and c < 9:
        b += 2
        c -= 6
    if c >= 9 and c < 12:
        a += 1
        c -= 9
    if c >= 12 and c < 15:
        a += 1
        b += 1
        c -= 12
    if c >= 15:
        a += 1
        b += 2
        c -= 15
    return nice_list[a][b][c]

nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
a = 0
b = 0
c = 0

my_list = [func(a,b,c) for c in range(18)]

print(my_list)


