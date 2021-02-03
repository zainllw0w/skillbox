violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

sound_time = 0

n = int(input('Какое количество песен добавить?: '))

for i in range(1, n+1):
    print('Введите название', i, 'песни: ', end='')
    song_name = input()
    for index in range(len(violator_songs)):
        if violator_songs[index][0] == song_name:
            sound_time += violator_songs[index][1]

print('Общее время звучания: ', sound_time, 'минут')
