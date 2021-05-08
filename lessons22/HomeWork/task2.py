zenFile = open('zen.txt', 'r')
createFile = open('newZen.txt', 'a')
my_list = [x for x in zenFile]
zenFile.close()

for i in range(len(my_list) - 1, 0, -1):
    createFile.write(my_list[i])

createFile.close()


