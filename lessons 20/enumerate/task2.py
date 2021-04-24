import random

first_list = [random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(10)]
second_list = [random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(10)]

print(first_list)
print(second_list)

first_dict = {i: x for i, x in enumerate(first_list)}
second_dict = {i: x for i, x in enumerate(second_list)}

print(first_dict)
print(second_dict)

