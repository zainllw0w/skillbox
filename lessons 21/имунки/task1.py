import random

def change_dict(dct):
    num = random.randint(1, 100)
    dct_2 = dict()
    for i_key, i_value in dct.items():
        if isinstance(i_value, list):
            i_value_2 = [x for x in i_value]
            i_value_2.append(num)
            dct_2[i_key] = i_value_2
        if isinstance(i_value, dict):
            i_value_3 = {x:y for x, y in i_value.items()}
            i_value_3[num] = i_key
            dct_2[i_key] = i_value_3
        if isinstance(i_value, set):
            i_value_4 = set()
            i_value_4.update(i_value)
            i_value_4.add(num)
            dct_2[i_key] = i_value_4
    dct.update(dct_2)


nums_list = [1, 2, 3]
some_dict = {1: 'text', 2: 'another text'}
uniq_nums = {1, 2, 3}
common_dict = {1: nums_list, 2: some_dict, 3: uniq_nums, 4: (10, 20, 30)}

change_dict(common_dict)

print(common_dict)
print(nums_list)
print(some_dict)
print(uniq_nums)

