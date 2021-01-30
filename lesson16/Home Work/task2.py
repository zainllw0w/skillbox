first_class = []
second_class = []

first_class.extend(list(range(160, 176, 2)))
second_class.extend(list(range(162, 180, 3)))

first_class.extend(second_class)

current = 1

for n in range(len(first_class)):
    for i in range(current, len(first_class)):
        if first_class[i] <= first_class[n]:
            first_class[i], first_class[n] = first_class[n], first_class[i]
    current += 1

print(first_class)