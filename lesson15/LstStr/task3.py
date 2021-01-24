word_list_count = [0, 0, 0]
word_search = []
text = ''

for _ in range(3):
    print('Введите', _ + 1, 'слово: ', end='')
    word = input()
    word_search.append(word)

while text != 'end':
    text = input('Слово из текста: ')
    for i in range(3):
        if word_search[i] == text:
            word_list_count[i] += 1

print('Подсчет слов в тексте')

for i in range(3):
    print(word_search[i], ':', word_list_count[i])
