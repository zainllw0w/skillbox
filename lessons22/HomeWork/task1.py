numFile = open('numbers.txt', 'r')
summ = 0
for i in numFile:
    for i_2 in i:
        if i_2.isdigit():
            summ += int(i)
numFile.close()
answerFile = open('answer.txt', 'w')
answerFile.write(str(summ))
answerFile.close()