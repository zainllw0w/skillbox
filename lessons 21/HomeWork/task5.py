def calculating_math_func(data, my_list = list(), result=1):
    if data <= len(my_list):
        return ((my_list[data-1])/data ** 3) ** 10
    if len(my_list) > 1:
        minn = len(my_list)+ 1
        result = my_list[-1]
    else:
        minn = 1
    for index in range(minn, data + 1):
        result *= index
        my_list.append(result)

    result /= data ** 3
    result = result ** 10
    return result

print(calculating_math_func(5))
print(calculating_math_func(6))
print(calculating_math_func(6))
