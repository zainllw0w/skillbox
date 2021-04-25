def sortii(cort):
    for i in cort:
        if isinstance(i, float):
            return cort
    return sorted(cort)


cort = 1, 5, 2.5, 4, 3

print(sortii(cort))