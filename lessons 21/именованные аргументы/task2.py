def f(n, lst = list()):
    lst.append(n)
    return lst

print(f(5))
print(f(10))
print(f(15))