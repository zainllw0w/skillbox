def f(data_1,data_2, c=0, my_list=list()):
    my_tuple = ((data_1[c], data_2[c]))
    my_list.append(my_tuple)
    if c == min(len(data_1), len(data_2)) - 1:
        return my_list
    return f(data_1, data_2, c+1, my_list)




data_1 = [1, 2, 2, 4]
data_2 = ('a', 'b', 'c')


print(f(data_1, data_2))
