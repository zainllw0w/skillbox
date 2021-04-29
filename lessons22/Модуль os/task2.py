import os
def print_path(path):
    for elem in os.listdir(path):
        print(elem)

data = os.path.abspath(os.path.join('/', 'games'))
print_path(data)