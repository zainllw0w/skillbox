violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}


time = float(0)

ask = int(input('Сколько песен запросить? '))

for i in range(1, ask +1):
    print('Название', i, 'песни: ', end='')
    song = input()
    time += violator_songs[song]
print('Общее время песен: ', time)