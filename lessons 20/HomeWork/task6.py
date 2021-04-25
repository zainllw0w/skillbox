import random

my_list = [random.randint(1, 9) for _ in range(10)]

print(my_list)

new_list = list()
second_list = list()
# for value in my_list:
#     new_list.append(value)
#     if len(new_list) == 2:
#         second_list.append(tuple(new_list))
#         new_list.clear()


for i in range(10):
    new_list.append(my_list[i])
    if i % 2 != 0:
        second_list.append(tuple(new_list))
        new_list.clear()



print(second_list)