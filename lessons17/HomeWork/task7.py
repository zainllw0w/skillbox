i = 1
my_list = []

while i < 5:
    my_list.append((list(range(i, i+10, 4))))
    i += 1

print(my_list)