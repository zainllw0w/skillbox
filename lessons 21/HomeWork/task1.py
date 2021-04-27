def f(n, c=1):
    print(c)
    if c == n:
        return c
    f(n, c+1)


f(12)