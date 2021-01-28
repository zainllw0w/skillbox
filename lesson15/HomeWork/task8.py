n = [1, 2, 3, 4, 5]
new = []
k = int(input('Сдвиг: '))

for _ in range(5):
        new.append(n[-k])
        k -= 1
print(n)
print(new)