my_list = [1, 4, -3, 0, 10]

for n in range(len(my_list)):
    for i in range(n, len(my_list)):
        if my_list[i] < my_list[n]:
            my_list[i], my_list[n] = my_list[n], my_list[i]



print(my_list)