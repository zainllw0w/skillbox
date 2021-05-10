def sorting(file):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v','w', 'x', 'y', 'z']
    count = 0
    curent_l = dict()
    for line in file:
        for letter in line:
            letter = letter.lower()
            if letter in alphabet:
                count += 1
                if letter in curent_l:
                    curent_l[letter] += 1
                else:
                    curent_l[letter] = 1
    return count, curent_l

def procent(count, ddict):
    for key, value in ddict.items():
        pros = value / count
        ddict[key] = round(pros, 3)
    return ddict

def refactor(ddict):
    revDicr = dict()
    for key, value in ddict.items():
        if value in revDicr:
            revDicr[value].append(key)
            revDicr[value] = sorted(revDicr[value])
        else:
            revDicr[value] = list()
            revDicr[value].append(key)
    return revDicr

def writeFile(ddict):
    file = open('analitic.txt', 'a')
    for key, value in ddict.items():
        for letter in value:
            string = f'{letter}: {key}\n'
            file.write(string)
    print('Файл записан!')
    file.close()



file = open('text8.txt', 'r')

count, ddict = sorting(file)
file.close()

ddict = procent(count, ddict)
ddict = refactor(ddict)

writeFile(ddict)

