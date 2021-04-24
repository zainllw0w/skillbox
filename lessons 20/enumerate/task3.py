def this_func(obj):
    if isinstance(obj, list):
        itog = [x for i, x in enumerate(obj) if i % 2 == 0]
    elif isinstance(obj, str):
        itog = [x for i, x in enumerate(obj) if i % 2 == 0]
    elif isinstance(obj, tuple):
        itog = [x for i, x in enumerate(obj) if i % 2 == 0]
    elif isinstance(obj, dict):
        itog = [x for i, x in enumerate(obj) if i % 2 == 0]

    return itog

text = input('Введите текст: ')

my_list = list(text)
my_dict = {1: text}
my_tuple = tuple(text)

print(my_list)
print(my_dict)
print(my_tuple)

print(this_func(my_dict))