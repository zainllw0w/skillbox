def sort(data, time):
    tt = False
    ft = True
    st = False
    is_find = True
    winers_name = set()
    index = 0
    while is_find:
        index += 1
        for key, values in data.items():
            if time[0 - index] == int(values[1]) and ft and values[0] not in winers_name:
                first_id = key
                ft = False
                st = True
                winers_name.add(values[0])
                first_i = index
            elif time[0 -index] == int(values[1]) and st and values[0] not in winers_name:
                second_id = key
                st = False
                tt = True
                winers_name.add(values[0])
                second_i = index
            elif time[0 -index] == int(values[1]) and tt and values[0] not in winers_name:
                three_id = key
                winers_name.add(values[0])
                is_find = False
                three_i = index
                break
    return first_id, second_id, three_id, first_i, second_i, three_i


n = int(input('Введите количество строк: '))

data = dict()
time_list = list()

for i in range(1, n+1):
    print(f'Введите {i} строку: ', end='')
    text = input().split()
    time = text[0]
    time_list.append(int(time))
    name = text[1]
    obj = [name, time]
    data[i] = tuple(obj)
f, s, t, fi, si, ti = sort(data, sorted(time_list))
time_list = sorted(time_list)

print('1 место занимает: {0}, с очками {1}'.format(data[f][0], time_list[-fi]))
print('2 место занимает: {0}, с очками {1}'.format(data[s][0], time_list[-si]))
print('3 место занимает: {0}, с очками {1}'.format(data[t][0], time_list[-ti]))