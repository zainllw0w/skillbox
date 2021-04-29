import os

file_name = 'admin.bat'
data = os.path.join('access', file_name)
print(data)
data = os.path.abspath(os.path.join('..', 'access', file_name))
print(data)