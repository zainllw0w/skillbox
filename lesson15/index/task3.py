n = int(input('Введите количество собак: '))
dogs_points = []


for _ in range(n):
    print('Введите очки ', _+1, 'собаки', end=' ')
    points = int(input())
    dogs_points.append(points)
print(dogs_points)


maximum = dogs_points[0]
minimum = dogs_points[0]
max_index = 0
min_index = 0


for i in range(n):
    if dogs_points[i] > maximum:
        maximum = dogs_points[i]
        max_index = i
    if dogs_points[i] < minimum:
        minimum = dogs_points[i]
        min_index = i


dogs_points[max_index], dogs_points[min_index] = dogs_points[min_index], dogs_points[max_index]

print('Переделаное: ', dogs_points)



