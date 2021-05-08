def fWord(file):
    wordCount = 0
    letterCount = 0
    minLetter = ''
    characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','t','u','v','w','x','y','z']
    minn = 99999
    letterDict = dict()
    file.seek(0)
    for line in file:
        for letter in line:

            if letter.lower() in characters:
                letter = letter.lower()
                letterCount += 1
                if letter in letterDict:
                    letterDict[letter] += 1
                else:
                    letterDict[letter] = 0

            if letter == ' ' or letter == '.':
                wordCount += 1
    for key, value in letterDict.items():
        if value < minn:
            minn = value
            minLetter = key

    return wordCount, letterCount, minLetter, minn

zenFile = open('zen.txt', 'r')
stringList = [x for x in zenFile]
string_count = len(stringList)
word, letter, mnLetter, countMnLetter = fWord(zenFile)

print(f'Количество строк: {string_count}\nКоличество слов: {word}\nКоличество букв: {letter}\nСамая редкая буква: {mnLetter} в количестве: {countMnLetter}')
