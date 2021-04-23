import random

def randnums(minn, maxx):
    a = []
    for _ in range(5):
        a.append(random.randint(minn, maxx))
    return tuple(a)




first_tuple = randnums(0, 5)
second_tuple = randnums(-5, 0)
three_tuple = first_tuple + second_tuple


print(first_tuple)
print(second_tuple)
print(three_tuple)

print('Количество 0 в третем кортеже: ', three_tuple.count(0))