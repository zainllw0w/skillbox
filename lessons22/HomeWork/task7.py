firstFile = open('first_tour.txt', 'r')


def getRaiting(file):
    raiting = ''
    for line in file:
        for letter in line:
            if letter.isdigit():
                raiting += letter
        return int(raiting)

def checkWho(file, raiting):
    createFile = open('second_tour.txt', 'a')
    count = 0
    allbals = set()
    data = dict()
    for line in file:
        if ' ' in line:
            wtf = line.split()
            if int(wtf[2]) > raiting:
                count += 1
                allbals.add(int(wtf[2]))
                data[count] = dict()
                data[count]['name'] = wtf[1]
                data[count]['surname'] = wtf[0]
                data[count]['rait'] = wtf[2]
    createFile.write(str(count)+'\n')
    count = 0
    for num in sorted(allbals, reverse=True):
        for key, value in data.items():
            if int(value['rait']) == num:
                count += 1
                outstring = '{}: {}. {} {}'.format(count, value['name'][0], value['surname'], value['rait'])
                createFile.write(outstring+'\n')






rait = getRaiting(firstFile)
checkWho(firstFile, rait)

