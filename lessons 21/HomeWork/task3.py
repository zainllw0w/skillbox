def f(n, k=1, i=1, my_list=[1]):
    if i == n:
        return my_list[-1]
    my_list.append(k)
    last_num = my_list[-2]
    return f(n, k+last_num, i+1)

print(f(6))