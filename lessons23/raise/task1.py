file = open('text.txt', 'r')
lenght = 0

for line in file:
    lenght = len(line)
    if line.endswith('\n'):
        lenght -= 1
    if lenght < 3:
        raise BaseException('В строке менее 3х символов')
